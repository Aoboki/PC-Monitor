@echo off
echo ===============================
echo Building PC Monitor...
echo ===============================

rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del *.spec 2>nul

"C:\Users\mukavesh\AppData\Local\Microsoft\WindowsApps\python3.11.exe" -m PyInstaller --onefile --windowed --add-data "LibreHardwareMonitor;LibreHardwareMonitor" main.py

pause