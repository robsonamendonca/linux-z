from flask import Flask, render_template
from analyzer import analyze_system
from scorer import calculate_score, recommend_distro

import requests
import time

app = Flask(__name__, 
            template_folder="../frontend/templates", 
            static_folder="../frontend/static")

# Version Cache
VERSION_CACHE = {"version": "0.0.0", "last_updated": 0}
CACHE_DURATION = 3600  # 1 hour

def get_latest_version():
    global VERSION_CACHE
    now = time.time()
    if now - VERSION_CACHE["last_updated"] < CACHE_DURATION:
        return VERSION_CACHE["version"]
    
    try:
        response = requests.get("https://api.github.com/repos/robsonamendonca/linux-z/tags", timeout=5)
        if response.status_code == 200:
            tags = response.json()
            if tags:
                VERSION_CACHE["version"] = tags[0]["name"]
                VERSION_CACHE["last_updated"] = now
                return VERSION_CACHE["version"]
    except Exception:
        pass
    
    return VERSION_CACHE["version"]

@app.route("/")
@app.route("/<lang>")
def index(lang="pt"):
    # Language dictionary
    translations = {
        "pt": {
            "title": "Linux-Z | Analisador de Hardware",
            "subtitle": "Análise de Hardware & Recomendação de Distro",
            "processor": "Processador",
            "memory": "Memória",
            "storage": "Armazenamento",
            "graphics": "Gráficos",
            "cores": "Núcleos",
            "threads": "Threads",
            "available": "Disponível",
            "total": "Total",
            "free": "Livre",
            "performance_score": "Pontuação de Desempenho",
            "based_on": "Baseado nas capacidades do hardware",
            "recommended": "Distribuições Recomendadas",
            "optimized": "Otimizado para o seu perfil de hardware.",
            "architecture": "Arquitetura",
            "cpu_info": "INFO_PROCESSADOR",
            "mem_stat": "ESTAT_MEMORIA",
            "gpu_strg": "GPU_ARMAZEM",
            "perf_score_tab": "PONTU_PERF",
            "distro_os": "DISTRO_SO",
            "model": "MODELO",
            "clock_freq": "FREQ_CLOCK",
            "alloc_res": "RECURSOS_ALOC",
            "sys_memory": "MEMORIA_SISTEMA",
            "capacity": "CAPACIDADE",
            "free_page": "PAGINA_LIVRE",
            "gpu_device": "DISPOSITIVO_GPU",
            "storage_unit": "UNIDADE_ARMAZEM",
            "drive_type": "TIPO_DRIVE",
            "total_size": "TAMANHO_TOTAL",
            "free_space": "ESPACO_LIVRE",
            "perf_index": "INDICE_PERF",
            "kernel_arch": "ARQU_KERNEL"
        },
        "en": {
            "title": "Linux-Z | Hardware Analyzer",
            "subtitle": "Hardware Analysis & Distro Recommendation",
            "processor": "Processor",
            "memory": "Memory",
            "storage": "Storage",
            "graphics": "Graphics",
            "cores": "Cores",
            "threads": "Threads",
            "available": "Available",
            "total": "Total",
            "free": "Free",
            "performance_score": "Performance Score",
            "based_on": "Based on hardware capabilities",
            "recommended": "Recommended Distributions",
            "optimized": "Optimized for your hardware profile.",
            "architecture": "Architecture",
            "cpu_info": "CPU_INFO",
            "mem_stat": "MEM_STAT",
            "gpu_strg": "GPU_STRG",
            "perf_score_tab": "PERF_SCORE",
            "distro_os": "DISTRO_OS",
            "model": "MODEL",
            "clock_freq": "CLOCK_FREQ",
            "alloc_res": "ALLOC_RES",
            "sys_memory": "SYS_MEMORY",
            "capacity": "CAPACITY",
            "free_page": "FREE_PAGE",
            "gpu_device": "GPU_DEVICE",
            "storage_unit": "STORAGE_UNIT",
            "drive_type": "DRIVE_TYPE",
            "total_size": "TOTAL_SIZE",
            "free_space": "FREE_SPACE",
            "perf_index": "PERF_INDEX",
            "kernel_arch": "KERNEL_ARCH"
        }
    }
    
    # Fallback to pt if invalid lang
    if lang not in translations:
        lang = "pt"
        
    system_info = analyze_system()
    score = calculate_score(system_info)
    distros = recommend_distro(score, system_info)

    return render_template(
        "index.html",
        system=system_info,
        score=score,
        distros=distros,
        t=translations[lang],
        current_lang=lang,
        version=get_latest_version()
    )

if __name__ == "__main__":
    print("🚀 Linux-Z starting at http://127.0.0.1:5000")
    app.run(debug=True)
