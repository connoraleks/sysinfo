# SysInfo Project

A simple CLI tool for querying basic system information, including CPU model, GPU model, and RAM amount.

## Setup

### Windows

1. Open PowerShell, navigate to the directory containing `setup.ps1`, and execute the following command:

    ```
    .\setup.ps1
    ```

2. To run the `sysinfo.py` script, activate the virtual environment and execute the desired query:

    ```
    .\venv\Scripts\Activate
    python sysinfo.py cpu
    python sysinfo.py gpu
    python sysinfo.py ram
    ```

### macOS/Linux

1. Open a terminal, navigate to the directory containing `setup.sh`, and execute the following command:

    ```
    bash setup.sh
    ```

2. To run the `sysinfo.py` script, activate the virtual environment and execute the desired query:

    ```
    source sysinfo_project/venv/bin/activate
    python sysinfo_project/sysinfo.py cpu
    python sysinfo_project/sysinfo.py gpu
    python sysinfo_project/sysinfo.py ram
    ```

## Usage

Run the script with one of the following arguments:

- `cpu`: Display the CPU model
- `gpu`: Display the GPU model(s)
- `ram`: Display the total RAM amount in GB
