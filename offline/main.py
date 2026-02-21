import os
import platform
import subprocess
import json
import sys

# Add core to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

import scorer
import recommender

def collect_data():
    system = platform.system()
    base_path = os.path.dirname(__file__)
    
    script_path = ""
    shell = False

    if system == "Linux":
        script_path = os.path.join(base_path, "linux", "collect.sh")
        # Ensure executable
        subprocess.run(["chmod", "+x", script_path])
        subprocess.run([script_path])
    elif system == "Windows":
        script_path = os.path.join(base_path, "windows", "collect.ps1")
        subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path])
    elif system == "Darwin": # macOS
        script_path = os.path.join(base_path, "macos", "collect.sh")
        subprocess.run(["chmod", "+x", script_path])
        subprocess.run([script_path])
    else:
        print(f"Unsupported system: {system}")
        return None

    json_path = os.path.join(os.getcwd(), "system_info.json")
    if os.path.exists(json_path):
        with open(json_path, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
        return data
    return None

def main():
    print("--- Linux-Z Offline Hardware Analysis ---")
    print("Collecting system information...")
    
    data = collect_data()
    
    if not data:
        print("Failed to collect system information.")
        return

    score, profile = scorer.calculate_score(data)
    recommendations = recommender.get_recommendations(score, profile, data.get('arch', ''))

    print("\nSystem details:")
    print(f"RAM: {round(data.get('ram_bytes', 0) / (1024**3), 2)} GB")
    print(f"CPU: {data.get('cpu_cores', 0)} cores ({data.get('cpu_model', 'Unknown')})")
    print(f"Arch: {data.get('arch', 'Unknown')}")
    print(f"Disk: {round(data.get('disk_bytes', 0) / (1024**3), 2)} GB")

    print(f"\nPerformance Score: {score}/100")
    print(f"Profile: {profile}")

    print("\nRecommended Distributions:")
    for dist in recommendations:
        print(f"- {dist}")

if __name__ == "__main__":
    main()
