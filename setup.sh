#!/bin/bash

echo "Creating project folder..."
# Create project folder
mkdir -p sysinfo_project
cd sysinfo_project

echo "Creating Python virtual environment..."
# Create Python virtual environment
python -m venv venv

echo "Activating virtual environment..."
# Activate virtual environment
source venv/bin/activate

echo "Installing required libraries (psutil and GPUtil)..."
# Install required libraries
pip install psutil GPUtil

echo "Creating main script file (sysinfo.py)..."
# Create main script file
cat > sysinfo.py << EOL
import sys
import psutil
import GPUtil
import platform

def cpu_info():
    cpu = platform.processor()
    print("CPU Model: {}".format(cpu))

def gpu_info():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        print("GPU Model: {}".format(gpu.name))

def ram_info():
    ram = psutil.virtual_memory()
    ram_total = ram.total / (1024 ** 3)
    print("Total RAM: {:.2f} GB".format(ram_total))

def main():
    if len(sys.argv) < 2:
        print("Usage: sysinfo.py [cpu|gpu|ram]")
        return

    query = sys.argv[1].lower()
    if query == "cpu":
        cpu_info()
    elif query == "gpu":
        gpu_info()
    elif query == "ram":
        ram_info()
    else:
        print("Invalid argument. Usage: sysinfo.py [cpu|gpu|ram]")

if __name__ == "__main__":
    main()
EOL

echo "Setup complete. To run the script, activate the virtual environment and execute 'python sysinfo.py [cpu|gpu|ram]'."
