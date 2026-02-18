import json
import os

def load_distros():
    path = os.path.join(os.path.dirname(__file__), "distros.json")
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return []

def calculate_score(system_info):
    score = 0
    
    ram = system_info["ram"]["total_gb"]
    cores = system_info["cpu"]["cores"] or 1
    is_ssd = system_info["disk"]["is_ssd"]
    gpu = system_info["gpu"]
    
    # RAM Score (max 4)
    if ram >= 16: score += 4
    elif ram >= 8: score += 3
    elif ram >= 4: score += 2
    else: score += 1
    
    # CPU Score (max 4)
    if cores >= 8: score += 4
    elif cores >= 4: score += 3
    elif cores >= 2: score += 2
    else: score += 1
    
    # SSD Bonus
    if is_ssd:
        score += 2
        
    # GPU Bonus
    if "NVIDIA" in gpu or "AMD" in gpu:
        score += 2
        
    return score

def recommend_distro(score, system_info):
    all_distros = load_distros()
    recommended = []
    
    ram = system_info["ram"]["total_gb"]
    cores = system_info["cpu"]["cores"] or 1
    gpu = system_info["gpu"]
    
    for d in all_distros:
        # Basic requirement check
        if ram >= d["min_ram_gb"] and cores >= d["min_cores"]:
            # Special logic for dedicated GPUs
            if d.get("gpu_required") == "NVIDIA" and "NVIDIA" not in gpu:
                continue
            
            recommended.append(d)
            
    # Tailor based on score
    if score >= 10:
        return [d["name"] for d in recommended if d["category"] in ["Gamer/Dev", "Cutting Edge", "Standard"]]
    elif score >= 6:
        return [d["name"] for d in recommended if d["category"] in ["Daily Driver", "Midweight", "Standard"]]
    else:
        return [d["name"] for d in recommended if d["category"] == "Lightweight"]

    return [d["name"] for d in recommended[:3]]
