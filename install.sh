#!/bin/bash

echo "Creating virtual environment..."
python -m venv sysinfo_project/venv

echo "Activating virtual environment..."
source sysinfo_project/venv/bin/activate

echo "Installing required packages..."
pip install -r requirements.txt

echo "Installing pyinstaller..."
pip install pyinstaller

echo "Creating executable with pyinstaller..."
pyinstaller --onefile sysinfo.py

echo "Moving the executable to sysinfo_project directory..."
mv dist/sysinfo sysinfo_project/

echo "Cleaning up..."
rm -rf dist
rm -rf __pycache__
rm -rf sysinfo.spec

echo "Setup complete. Activate the virtual environment and use the 'sysinfo' command."
