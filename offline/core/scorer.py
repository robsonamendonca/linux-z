import json

def calculate_score(data):
    """
    Calculates a performance score (0-100) based on hardware data.
    """
    ram_gb = data.get('ram_bytes', 0) / (1024**3)
    cpu_cores = data.get('cpu_cores', 1)
    disk_gb = data.get('disk_bytes', 0) / (1024**3)
    arch = data.get('arch', '64-bit')

    # RAM Score (40%)
    if ram_gb < 2:
        ram_score = 10
    elif ram_gb < 4:
        ram_score = 30
    elif ram_gb < 8:
        ram_score = 60
    else:
        ram_score = 100

    # CPU Score (30%)
    if cpu_cores == 1:
        cpu_score = 20
    elif cpu_cores == 2:
        cpu_score = 40
    elif cpu_cores <= 4:
        cpu_score = 70
    else:
        cpu_score = 100

    # Disk Score (20%)
    if disk_gb < 40:
        disk_score = 20
    elif disk_gb < 120:
        disk_score = 50
    elif disk_gb < 250:
        disk_score = 80
    else:
        disk_score = 100

    # Architecture Score (10%)
    arch_score = 100 if '64' in arch else 40

    total_score = (ram_score * 0.4) + (cpu_score * 0.3) + (disk_score * 0.2) + (arch_score * 0.1)
    
    profile = "Low-end"
    if total_score > 70:
        profile = "High-end"
    elif total_score > 40:
        profile = "Mid-range"

    return round(total_score), profile

if __name__ == "__main__":
    # Test with dummy data
    test_data = {
        "ram_bytes": 4 * (1024**3),
        "cpu_cores": 2,
        "arch": "64-bit",
        "disk_bytes": 128 * (1024**3)
    }
    print(calculate_score(test_data))
