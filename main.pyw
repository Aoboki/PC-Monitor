import ctypes
import sys
import os
import time


def run_as_admin():
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
    except:
        is_admin = False

    if not is_admin:

        # путь к текущему скрипту
        script = os.path.abspath(sys.argv[0])

        # параметры командной строки
        params = " ".join(f'"{a}"' for a in sys.argv[1:])

        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            f'"{script}" {params}',
            None,
            1
        )

        sys.exit()


# Запускаем программу от имени администратора
run_as_admin()


# ==========================================================
# PC Monitor v2.0
# main.py
# ==========================================================

import os
import clr

# ==========================================================
# Подключение LibreHardwareMonitor
# ==========================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DLL_PATH = os.path.join(
    SCRIPT_DIR,
    "LibreHardwareMonitor",
    "LibreHardwareMonitorLib.dll"
)

clr.AddReference(DLL_PATH)

from LibreHardwareMonitor.Hardware import Computer

# ==========================================================
# Класс Monitor
# ==========================================================

class Monitor:

    def __init__(self):

        self.cpu_name = "CPU"
        self.gpu_name = "GPU"

        self.pc = Computer()

        self.pc.IsCpuEnabled = True
        self.pc.IsGpuEnabled = True
        self.pc.IsMemoryEnabled = True
        self.pc.IsStorageEnabled = True
        self.pc.IsMotherboardEnabled = True

        self.pc.Open()

        # Здесь будут храниться все найденные датчики
        self.sensors = {}

    # ------------------------------------------------------

    def update(self):

        self.sensors.clear()

        for hardware in self.pc.Hardware:

            if str(hardware.HardwareType) == "Cpu":
                self.cpu_name = hardware.Name

            if str(hardware.HardwareType) == "GpuNvidia":
                self.gpu_name = hardware.Name

            elif (
                str(hardware.HardwareType) == "GpuAmd"
                and self.gpu_name == "GPU"
            ):
                self.gpu_name = hardware.Name

            elif (
                str(hardware.HardwareType) == "GpuIntel"
                and self.gpu_name == "GPU"
            ):
                self.gpu_name = hardware.Name

            hardware.Update()

            # Основные датчики
            for sensor in hardware.Sensors:

                key = (str(sensor.SensorType), sensor.Name)
                self.sensors[key] = sensor.Value

            # Вложенные устройства
            for sub in hardware.SubHardware:

                sub.Update()

                for sensor in sub.Sensors:

                    key = (str(sensor.SensorType), sensor.Name)
                    self.sensors[key] = sensor.Value

    # ------------------------------------------------------

    def sensor(self, sensor_type, sensor_name):

        return self.sensors.get(
            (sensor_type, sensor_name),
            None
        )

    # ------------------------------------------------------
    

    

    def get_data(self):

 
        self.update()

        data = {}

        # CPU
        data["CPU Load"] = self.sensor("Load", "CPU Total")

        # Все температуры CPU
        
        
       
        for (stype, name), value in self.sensors.items():

            if stype != "Temperature":
                continue

            if name == "CPU Package":
                data[name] = value

            elif (
                name.startswith("CPU Core")
                and "Distance" not in name
                and "TjMax" not in name
            ):
                data[name] = value

        # GPU
        data["GPU Temperature"] = self.sensor(
            "Temperature",
            "GPU Core"
        )

        data["GPU Hot Spot"] = self.sensor(
            "Temperature",
            "GPU Hot Spot"
        )

        return data


# ==========================================================
# Главная программа
# ==========================================================

if __name__ == "__main__":

    from gui import MonitorGUI

    monitor = Monitor()

    gui = MonitorGUI(monitor)

    gui.start()
