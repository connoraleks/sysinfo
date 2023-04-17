import sys
import psutil
import GPUtil
import platform
import os
import socket
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from rounded_frame import RoundedFrame



def get_system_info():
    info = ["System Information:", "--------------------",
            f"Operating System: {platform.system()} {platform.release()}",
            f"Platform: {platform.platform()}",
            f"Node: {platform.node()}",
            f"Hostname: {socket.gethostname()}",
            f"IP Address: {socket.gethostbyname(socket.gethostname())}"]
    return "\n".join(info)


def get_cpu_info():
    cpu = platform.processor()
    cpu_cores = os.cpu_count()
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq()
    cpu_min_freq = cpu_freq.min
    cpu_max_freq = cpu_freq.max
    cpu_current_freq = cpu_freq.current

    info = ["CPU Information:", "----------------",
            f"CPU Model: {cpu}",
            f"CPU Cores: {cpu_cores}",
            f"CPU Usage: {cpu_usage}%",
            f"CPU Frequency: {cpu_current_freq} MHz",
            f"CPU Min Frequency: {cpu_min_freq} MHz",
            f"CPU Max Frequency: {cpu_max_freq} MHz"]
    return "\n".join(info)


def get_gpu_info():
    gpus = GPUtil.getGPUs()
    info = ["GPU Information:", "----------------"]

    for i, gpu in enumerate(gpus):
        info.extend([f"GPU {i + 1}: {gpu.name}",
                    f"  GPU ID: {gpu.id}",
                    f"  GPU Load: {gpu.load * 100:.2f}%",
                    f"  GPU Temperature: {gpu.temperature} °C",
                    f"  GPU Memory Total: {gpu.memoryTotal:.2f} MB",
                    f"  GPU Memory Used: {gpu.memoryUsed:.2f} MB",
                    f"  GPU Memory Free: {gpu.memoryFree:.2f} MB"])

    return "\n".join(info)


def get_ram_info():
    ram = psutil.virtual_memory()
    ram_total = ram.total / (1024 ** 3)
    ram_available = ram.available / (1024 ** 3)
    ram_used = ram.used / (1024 ** 3)
    ram_percent_used = ram.percent

    info = ["RAM Information:", "----------------",
            f"Total RAM: {ram_total:.2f} GB",
            f"Available RAM: {ram_available:.2f} GB",
            f"Used RAM: {ram_used:.2f} GB",
            f"RAM Usage: {ram_percent_used}%"]
    return "\n".join(info)


def get_storage_info():
    partitions = psutil.disk_partitions()
    info = ["Storage Information:", "---------------------"]

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        total_space = usage.total / (1024 ** 3)
        used_space = usage.used / (1024 ** 3)
        free_space = usage.free / (1024 ** 3)
        percent_used = usage.percent

        info.extend([f"Device: {partition.device}",
                    f"  Mountpoint: {partition.mountpoint}",
                    f"  File System: {partition.fstype}",
                    f"  Total Space: {total_space:.2f} GB",
                    f"  Used Space: {used_space:.2f} GB",
                    f"  Free Space: {free_space:.2f} GB",
                    f" Space Usage: {percent_used}%"])
        return "\n".join(info)

def get_network_info():
    interfaces = psutil.net_if_addrs()
    info = ["Network Information:", "-------------------"]

    for interface, addrs in interfaces.items():
        info.append(f"{interface}:")
        for addr in addrs:
            info.append(f"  {addr.family.name}: {addr.address}")
            if addr.broadcast:
                info.append(f"  Broadcast: {addr.broadcast}")
            if addr.netmask:
                info.append(f"  Netmask: {addr.netmask}")
            if addr.ptp:
                info.append(f"  PTP: {addr.ptp}")
        info.append("")

    return "\n".join(info)

def analyze_system_performance():
    recommendations = []

    # CPU usage analysis
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > 90:
        recommendations.append("High CPU usage detected. Consider upgrading your CPU or closing unnecessary programs.")

    # RAM usage analysis
    ram = psutil.virtual_memory()
    ram_percent_used = ram.percent
    if ram_percent_used > 90:
        recommendations.append("High RAM usage detected. Consider upgrading your RAM or closing unnecessary programs.")

    # Network usage analysis
    network_stats = psutil.net_io_counters()
    network_sent_bytes = network_stats.bytes_sent
    network_recv_bytes = network_stats.bytes_recv
    if network_sent_bytes + network_recv_bytes > 1e12:  # 1 TB
        recommendations.append("High network usage detected. Consider upgrading your network hardware or reducing network-intensive activities.")

    # GPU usage analysis
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        if gpu.load > 0.9:
            recommendations.append(f"High GPU usage detected for {gpu.name}. Consider upgrading your GPU or closing GPU-intensive programs.")

    # Disk usage analysis
    partitions = psutil.disk_partitions()
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        if usage.percent > 90:
            recommendations.append(f"High disk usage detected for {partition.device}. Consider upgrading your storage device or freeing up space.")

    return recommendations

def display_info_gui():
    window = tk.Tk()
    window.title("SysInfo")
    window.geometry("800x600")
    window.configure(bg="white", highlightthickness=0)
    window.attributes("-alpha", 0.9)  # Set the window transparency to 90%

    notebook = ttk.Notebook(window)
    notebook.pack(expand=True, fill="both")

    # Create the tabs
    system_tab = RoundedFrame(notebook, bg="white")
    cpu_tab = RoundedFrame(notebook, bg="white")
    memory_tab = RoundedFrame(notebook, bg="white")
    disk_tab = RoundedFrame(notebook, bg="white")
    network_tab = RoundedFrame(notebook, bg="white")
    recommendations_tab = RoundedFrame(notebook, bg="white")



    # Add the tabs to the notebook
    notebook.add(system_tab, text="System")
    notebook.add(cpu_tab, text="CPU")
    notebook.add(memory_tab, text="Memory")
    notebook.add(disk_tab, text="Disk")
    notebook.add(network_tab, text="Network")
    notebook.add(recommendations_tab, text="Recommendations")

    # Add labels with info to the tabs
    system_info_label = ttk.Label(system_tab._canvas, text=get_system_info(), style="InfoText.TLabel", wraplength=750, justify="left", anchor="nw")
    system_info_label.place(x=10, y=10)

    cpu_info_label = ttk.Label(cpu_tab._canvas, text=get_cpu_info(), style="InfoText.TLabel", wraplength=750, justify="left", anchor="nw")
    cpu_info_label.place(x=10, y=10)

    memory_info_label = ttk.Label(memory_tab._canvas, text=get_ram_info(), style="InfoText.TLabel", wraplength=750, justify="left", anchor="nw")
    memory_info_label.place(x=10, y=10)

    disk_info_label = ttk.Label(disk_tab._canvas, text=get_storage_info(), style="InfoText.TLabel", wraplength=750, justify="left", anchor="nw")
    disk_info_label.place(x=10, y=10)

    network_info_label = ttk.Label(network_tab._canvas, text=get_network_info(), style="InfoText.TLabel", wraplength=750, justify="left", anchor="nw")
    network_info_label.place(x=10, y=10)
    
    recommendations_text = "\n".join(analyze_system_performance())
    recommendations_label = ttk.Label(recommendations_tab._canvas, text=recommendations_text, style="InfoText.TLabel", wraplength=750, justify="left", anchor="nw")
    recommendations_label.place(x=10, y=10)


    window.mainloop()



def run_cli():
    while True:
        print("\nSelect an option to display information:")
        print("1. System")
        print("2. CPU")
        print("3. GPU")
        print("4. RAM")
        print("5. Storage")
        print("q. Quit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print(get_system_info())
        elif choice == "2":
            print(get_cpu_info())
        elif choice == "3":
            print(get_gpu_info())
        elif choice == "4":
            print(get_ram_info())
        elif choice == "5":
            print(get_storage_info())
        elif choice.lower() == "q":
            break
        else:
            print("\nInvalid choice, please try again.")

def run_gui():
    display_info_gui()
    
def main():
    if len(sys.argv) > 1 and sys.argv[1] == "-cli":
        run_cli()
    else:
        run_gui()

if __name__ == "__main__":
    main()
