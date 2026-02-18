from flask import Flask, render_template
from analyzer import analyze_system
from scorer import calculate_score, recommend_distro

app = Flask(__name__, 
            template_folder="../frontend/templates", 
            static_folder="../frontend/static")

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
            "architecture": "Arquitetura"
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
            "architecture": "Architecture"
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
        current_lang=lang
    )

if __name__ == "__main__":
    print("🚀 Linux-Z starting at http://127.0.0.1:5000")
    app.run(debug=True)
