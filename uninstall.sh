#!/bin/bash

echo "Uninstalling SysInfo Project..."

# Check if sysinfo_project folder exists
if [ -d "sysinfo_project" ]; then
    # Remove sysinfo_project folder
    echo "Removing SysInfo Project folder..."
    rm -rf sysinfo_project
    echo "SysInfo Project has been uninstalled."
else
    echo "SysInfo Project folder not found. No action taken."
fi
