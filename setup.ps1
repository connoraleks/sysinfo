# Create project folder
Write-Host "Creating project folder..."
New-Item -ItemType Directory -Force -Path sysinfo_project
Set-Location sysinfo_project

# Create Python virtual environment
Write-Host "Creating Python virtual environment..."
python -m venv venv

# Activate virtual environment
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate

# Install required libraries
Write-Host "Installing required libraries (psutil and GPUtil)..."
pip install psutil GPUtil

# Create main script file
Write-Host "Creating main script file (sysinfo.py)..."
@"
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
"@ | Out-File -FilePath sysinfo.py
    
Write-Host "Setup complete. To run the script, activate the virtual environment and execute 'python sysinfo.py [cpu|gpu|ram]'."
    
