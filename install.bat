@echo off
title PC Monitor - Install Dependencies

echo ======================================
echo Installing Python dependencies...
echo ======================================
echo.

where python >nul 2>nul
if %errorlevel%==0 (
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    goto end
)

where py >nul 2>nul
if %errorlevel%==0 (
    py -m pip install --upgrade pip
    py -m pip install -r requirements.txt
    goto end
)

echo Python is not installed or not found in PATH.
echo Please install Python 3.11 or newer.

:end
pause