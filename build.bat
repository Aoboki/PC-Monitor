@echo off
title PC Monitor - Build

echo Cleaning...
rmdir /s /q build 2>nul
rmdir /s /q dist 2>nul
del *.spec 2>nul

echo Building...

python -m PyInstaller ^
--onefile ^
--windowed ^
--name "PC Monitor" ^
--add-data "LibreHardwareMonitor;LibreHardwareMonitor" ^
main.py

echo.
echo Build complete.
pause