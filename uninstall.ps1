Write-Host "Uninstalling SysInfo Project..."

# Check if sysinfo_project folder exists
if (Test-Path -Path .\sysinfo_project) {
    # Remove sysinfo_project folder
    Write-Host "Removing SysInfo Project folder..."
    Remove-Item -Recurse -Force .\sysinfo_project
    Write-Host "SysInfo Project has been uninstalled."
} else {
    Write-Host "SysInfo Project folder not found. No action taken."
}
