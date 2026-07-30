# ==========================================================
# PC Monitor v2.0
# gui.py
# ==========================================================

import customtkinter as ctk
from datetime import datetime


class MonitorGUI:

    # ------------------------------------------------------

    def __init__(self, monitor):

        self.monitor = monitor

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.window = ctk.CTk()

        self.window.title("PC Monitor")
        self.window.minsize(420, 200)
        self.window.resizable(False, False)

        # ---------- Заголовок ----------

        title = ctk.CTkLabel(
            self.window,
            text="PC Monitor",
            font=("Arial", 24, "bold")
        )

        title.pack(pady=10)

        # ---------- CPU ----------

        self.cpu_frame = ctk.CTkFrame(self.window)
        self.cpu_frame.pack(fill="x", padx=15, pady=5)

        self.cpu_title = ctk.CTkLabel(
            self.cpu_frame,
            text="CPU",
            font=("Arial", 18, "bold")
        )

        self.cpu_title.pack(anchor="w", padx=10, pady=5)

        # ---------- GPU ----------

        self.gpu_frame = ctk.CTkFrame(self.window)
        self.gpu_frame.pack(fill="x", padx=15, pady=5)

        self.gpu_title = ctk.CTkLabel(
            self.gpu_frame,
            text="GPU",
            font=("Arial", 18, "bold")
        )

        self.gpu_title.pack(anchor="w", padx=10, pady=5)

        # Здесь будут храниться все Label
        self.labels = {}

        # ---------- Время ----------

        self.time_label = ctk.CTkLabel(
            self.window,
            text="",
            font=("Arial", 14)
        )

        self.time_label.pack(pady=10)

    # ------------------------------------------------------

    def create_label(self, parent, name):

        label = ctk.CTkLabel(
            parent,
            text=f"{name}: ---",
            font=("Consolas", 16),
            anchor="w"
        )

        label.pack(fill="x", padx=20, pady=2)

        self.labels[name] = label

    # ------------------------------------------------------

    def format_value(self, name, value):

        if value is None:
            return "Недоступно"

        if (
            "Temperature" in name
            or "Hot Spot" in name
            or "Package" in name
            or "Core" in name
        ):
            return f"{value:.1f} °C"

        if "Load" in name:
            return f"{value:.1f} %"

        return str(value)

    # ------------------------------------------------------

    def update_screen(self):

        data = self.monitor.get_data()

        self.cpu_title.configure(text=self.monitor.cpu_name)
        self.gpu_title.configure(text=self.monitor.gpu_name)

        # Создаём новые Label автоматически
        for name in data:

            if name not in self.labels:

                if "GPU" in name:
                    parent = self.gpu_frame
                else:
                    parent = self.cpu_frame

                self.create_label(parent, name)

        # Обновляем значения
        for name, value in data.items():

            text = self.format_value(name, value)

            self.labels[name].configure(
                text=f"{name}: {text}"
            )



        self.window.after(10, self.update_screen)

    # ------------------------------------------------------

    def start(self):

        self.update_screen()

        self.window.update_idletasks()

        width = self.window.winfo_reqwidth()
        height = self.window.winfo_reqheight()

        self.window.geometry(f"{width}x{height}")

        self.window.mainloop()   # ← Этой строки не хватает
