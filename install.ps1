# setup.ps1

# Create a virtual environment
Write-Host "Creating virtual environment..."
python -m venv venv

# Activate the virtual environment
Write-Host "Activating virtual environment..."
. .\venv\Scripts\Activate

# Install the required packages
Write-Host "Installing required packages..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Create an executable using PyInstaller
Write-Host "Creating an executable using PyInstaller..."
pyinstaller --onefile code\sysinfo_main.py --name sysinfo

# Move the created executable to the root directory
Move-Item .\dist\sysinfo.exe .\sysinfo.exe

# Cleanup: remove build, dist, and __pycache__ folders and the .spec file
Write-Host "Cleaning up..."
Remove-Item -Recurse -Force .\build
Remove-Item -Recurse -Force .\dist
Remove-Item .\sysinfo.spec

# Remove the virtual environment
Write-Host "Removing virtual environment..."
deactivate
Remove-Item -Recurse -Force .\venv

# Inform the user that the setup is complete
Write-Host "Setup complete. Use the 'sysinfo.exe' to run the program."
