# PC Monitor

A lightweight Windows hardware monitoring application written in Python using LibreHardwareMonitor.

## Features

- CPU usage
- CPU package temperature
- CPU core temperatures
- GPU temperature
- GPU Hot Spot
- Automatic hardware detection
- Modern CustomTkinter interface
- Standalone EXE support

## Requirements

- Windows 10 / Windows 11
- Python 3.11+

## Installation

Install dependencies:

```bash
install.bat
```

or

```bash
pip install -r requirements.txt
```

## Build

```bash
build.bat
```

or

```bash
python -m PyInstaller --onefile --windowed --add-data "LibreHardwareMonitor;LibreHardwareMonitor" main.py
```

## Screenshot

*(Add a screenshot here later.)*

## License

MIT License
