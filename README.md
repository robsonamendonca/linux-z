[![Version](https://img.shields.io/badge/version-v0.13.0-blue)](https://github.com/robsonamendonca/linux-z/releases)
# 🐧 Linux-Z

**Linux-Z** é um analisador de hardware de código aberto inspirado no CPU-Z, projetado para recomendar a distribuição Linux ideal com base no desempenho e nas capacidades do seu hardware.

Se você está procurando uma distro leve para uma máquina antiga ou uma configuração poderosa para jogos e desenvolvimento, o Linux-Z analisa sua CPU, RAM, GPU e Armazenamento para te dar o melhor conselho.

---

## ✨ Funcionalidades

- **🔍 Detecção de Hardware Avançada**: Detecta automaticamente CPU (modelo, núcleos, threads), RAM, Armazenamento (SSD/HDD) e GPU (NVIDIA/AMD/Intel).
- **📊 Pontuação de Desempenho**: Calcula uma pontuação de hardware (0-12) para categorizar sua máquina.
- **🐧 Recomendações Inteligentes**: Sugere distribuições baseadas em requisitos reais de hardware e perfis de usuário.
- **🎨 Interface Web Premium**: Um dashboard moderno com design glassmorphism e modo escuro.
- **💻 CLI de Alta Qualidade**: Uma bela interface de terminal alimentada pela biblioteca `rich`.

---

## 🛠️ Requisitos

- **Python 3.8+**
- **pip** (Gerenciador de pacotes do Python)
- **Linux** (Recomendado para precisão total na detecção de hardware)

---

## 🚀 Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/robsonamendonca/linux-z.git
   cd linux-z
   ```

2. **Instale as dependências**:

   No Windows (PowerShell):
   ```powershell
   python -m pip install -r backend/requirements.txt
   ```
   No Debian/Ubuntu e distribuições linux modernas que seguem o padrão [PEP 668](https://peps.python.org/pep-0668).
   ```bash
   pip install --break-system-packages -r backend/requirements.txt
   ```
   Em outras distros Linux/macOS:
   ```bash
   pip install -r backend/requirements.txt
   ```

---

## 🎮 Como Rodar

### 🌐 Versão Web (Dashboard Premium)
1. Navegue até o diretório backend:
   ```bash
   cd backend
   ```
2. Inicie o servidor Flask:
   ```bash
   python app.py
   ```
3. Abra seu navegador e visite: `http://127.0.0.1:5000`
4. **Idioma**: Use os botões no canto superior direito para alternar entre **PT-BR** e **EN**.

### 🖥️ Versão CLI (Interface de Terminal)
1. Na raiz do projeto, execute:
   ```bash
   # Padrão (Português)
   python cli/linuxz_cli.py
   
   # Para Inglês (English)
   python cli/linuxz_cli.py --lang en
   ```

---

## 🧪 Testes e Verificação

Para verificar se o sistema está detectando seu hardware corretamente:

1. **Verifique a Saída CLI**: Execute a versão CLI e compare a tabela "System Information" com suas especificações reais.
2. **Valide as Recomendações**:
   - Máquinas com < 4GB de RAM devem ver recomendações **Leves** (Puppy, AntiX).
   - Máquinas com GPUs NVIDIA devem ver o **Pop!_OS** na lista.
   - Máquinas com SSDs receberão uma pontuação de desempenho maior.
3. **Logs**: Verifique o terminal onde o `app.py` está rodando para quaisquer erros do Flask ou avisos de detecção de hardware.

---

## 📁 Estrutura do Projeto

```text
linux-z/
├── backend/            # Lógica central, analisador e API Flask
│   ├── analyzer.py     # Lógica de detecção de hardware
│   ├── scorer.py       # Mecanismo de recomendação
│   ├── distros.json    # Banco de dados de distros
│   └── app.py          # Servidor Web
├── frontend/           # Ativos da interface Web
│   ├── templates/      # HTML (Jinja2)
│   └── static/         # CSS e imagens
├── cli/                # Interface de terminal
└── requirements.txt    # Dependências do projeto
```

---

## 📜 Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar a detecção de hardware ou adicionar novas distros ao banco de dados.
