# uninstall.ps1

# Remove the sysinfo executable
if (Test-Path -Path ".\sysinfo.exe") {
    Write-Host "Removing sysinfo executable..."
    Remove-Item -Path ".\sysinfo.exe"
}

# Deactivate the virtual environment if active
if (Test-Path -Path "venv") {
    Write-Host "Deactivating virtual environment..."
    & ".\venv\Scripts\deactivate"
}

# Remove the virtual environment
if (Test-Path -Path "venv") {
    Write-Host "Removing virtual environment..."
    Remove-Item -Recurse -Force "venv"
}

# Remove the build directory
if (Test-Path -Path "build") {
    Write-Host "Removing build directory..."
    Remove-Item -Recurse -Force "build"
}

# Remove sysinfo.spec
if (Test-Path -Path "sysinfo.spec") {
    Write-Host "Removing sysinfo.spec..."
    Remove-Item -Path "sysinfo.spec"
}


Write-Host "Uninstall complete."
