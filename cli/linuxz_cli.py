import sys
import os
import argparse

# Add backend to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich import print as rprint
except ImportError:
    print("Error: 'rich' library not found. Run 'pip install rich' for the best experience.")
    sys.exit(1)

from analyzer import analyze_system
from scorer import calculate_score, recommend_distro

def run_cli():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Linux-Z Premium CLI - Hardware Analyzer & Distro Recommender")
    parser.add_argument("--lang", choices=["pt", "en"], default="pt", help="Language choice (pt for Portuguese, en for English)")
    args = parser.parse_args()

    # Translations
    translations = {
        "pt": {
            "title": "🐧 Linux-Z Premium CLI",
            "status": "Analisando hardware do sistema...",
            "table_title": "Informações do Sistema",
            "col_comp": "Componente",
            "col_det": "Detalhes",
            "score": "Pontuação de Desempenho",
            "rec": "Distribuições Linux Recomendadas",
            "web_hint": "Execute a versão web: 'python backend/app.py'",
            "cores_threads": "Núcleos / Threads",
            "available": "Disponível",
            "arch": "Arquitetura"
        },
        "en": {
            "title": "🐧 Linux-Z Premium CLI",
            "status": "Analyzing system hardware...",
            "table_title": "System Information",
            "col_comp": "Componente",
            "col_det": "Details",
            "score": "Performance Score",
            "rec": "Recommended Linux Distributions",
            "web_hint": "Run the web version: 'python backend/app.py'",
            "cores_threads": "Cores / Threads",
            "available": "Available",
            "arch": "Architecture"
        }
    }

    t = translations[args.lang]
    console = Console()
    
    with console.status(f"[bold green]{t['status']}") as status:
        system = analyze_system()
        score = calculate_score(system)
        distros = recommend_distro(score, system)

    rprint(Panel.fit(f"[bold blue]{t['title']}[/bold blue]", border_style="blue"))

    # Hardware Table
    table = Table(title=t['table_title'], title_style="bold magenta")
    table.add_column(t['col_comp'], style="cyan")
    table.add_column(t['col_det'], style="white")

    table.add_row("CPU", f"{system['cpu']['model']}")
    table.add_row(t['cores_threads'], f"{system['cpu']['cores']} / {system['cpu']['threads']}")
    table.add_row("RAM", f"{system['ram']['total_gb']} GB ({system['ram']['available_gb']} GB {t['available']})")
    table.add_row("Disk", f"{system['disk']['total_gb']} GB ({'SSD' if system['disk']['is_ssd'] else 'HDD'})")
    table.add_row("GPU", f"{system['gpu']}")
    table.add_row(t['arch'], f"{system['arch']}")

    console.print(table)

    # Score
    score_color = "green" if score >= 8 else "yellow" if score >= 5 else "red"
    rprint(f"\n[bold]{t['score']}:[/bold] [{score_color}]{score}/12[/{score_color}]")

    # Recommendations
    rprint(f"\n[bold underline]{t['rec']}:[/bold underline]")
    for d in distros:
        rprint(f" • [bold green]{d}[/bold green]")

    rprint(f"\n[dim]{t['web_hint']}[/dim]")

if __name__ == "__main__":
    run_cli()
