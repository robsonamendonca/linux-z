import platform
import psutil
import os
import subprocess

def get_cpu_info():
    # Use platform first, then try to get more specific info
    model = platform.processor()
    if not model or model == "unknown":
        try:
            # On Linux, /proc/cpuinfo is better
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "model name" in line:
                        model = line.split(":")[1].strip()
                        break
        except:
            pass
    
    return {
        "model": model,
        "cores": psutil.cpu_count(logical=False),
        "threads": psutil.cpu_count(logical=True),
        "frequency": psutil.cpu_freq().max if psutil.cpu_freq() else None
    }

def get_ram_info():
    ram = psutil.virtual_memory()
    return {
        "total_gb": round(ram.total / (1024**3), 2),
        "available_gb": round(ram.available / (1024**3), 2)
    }

def get_disk_info():
    disk = psutil.disk_usage('/')
    
    # Try to detect if it's SSD
    is_ssd = False
    try:
        # Simplistic check for Linux
        with open("/sys/block/sda/queue/rotational", "r") as f:
            is_ssd = f.read().strip() == "0"
    except:
        pass

    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "free_gb": round(disk.free / (1024**3), 2),
        "is_ssd": is_ssd
    }

def get_gpu_info():
    # Attempt to detect GPU using lspci on Linux
    gpu = "Unknown / Integrated"
    try:
        output = subprocess.check_output("lspci | grep -i vga", shell=True).decode()
        if "NVIDIA" in output.upper():
            gpu = "NVIDIA Dedicated GPU"
        elif "AMD" in output.upper() or "ATI" in output.upper():
            gpu = "AMD Dedicated GPU"
        elif "INTEL" in output.upper():
            gpu = "Intel Integrated Graphics"
    except:
        pass
    return gpu

def get_architecture():
    return platform.architecture()[0]

def analyze_system():
    return {
        "cpu": get_cpu_info(),
        "ram": get_ram_info(),
        "disk": get_disk_info(),
        "gpu": get_gpu_info(),
        "arch": get_architecture()
    }
