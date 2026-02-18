# 🐧 Linux-Z

**Linux-Z** is an open-source hardware analyzer inspired by CPU-Z, designed to recommend the ideal Linux distribution based on your system's performance and hardware capabilities.

Whether you're looking for a lightweight distro for an old machine or a powerful setup for gaming and development, Linux-Z analyzes your CPU, RAM, GPU, and Storage to give you the best advice.

---

## ✨ Features

- **🔍 Advanced Hardware Detection**: Automatically detects CPU (model, cores, threads), RAM, Storage (SSD/HDD), and GPU (NVIDIA/AMD/Intel).
- **📊 Performance Scoring**: Calculates a hardware score (0-12) to categorize your machine.
- **🐧 Smart Recommendations**: Suggests distributions based on real hardware requirements and user profiles.
- **🎨 Premium Web UI**: A modern dashboard with a glassmorphism design and dark mode.
- **💻 High-End CLI**: A beautiful terminal interface powered by the `rich` library.

---

## 🛠️ Requirements

- **Python 3.8+**
- **pip** (Python package manager)
- **Linux** (Recommended for full hardware detection accuracy)

---

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/robsonamendonca/linux-z.git
   cd linux-z
   ```

2. **Install dependencies**:
   ```bash
   pip install -r backend/requirements.txt
   ```

---

## 🎮 How to Run

### 🌐 Web Version (Premium Dashboard)
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Start the Flask server:
   ```bash
   python app.py
   ```
3. Open your browser and visit: `http://127.0.0.1:5000`
4. **Language**: Use the buttons in the top right corner to switch between **PT-BR** and **EN**.

### 🖥️ CLI Version (Terminal Interface)
1. From the project root, run:
   ```bash
   # Default (Portuguese)
   python cli/linuxz_cli.py
   
   # For English
   python cli/linuxz_cli.py --lang en
   ```

---

## 🧪 Testing & Verification

To verify if the system is detecting your hardware correctly:

1. **Check the CLI Output**: Run the CLI version and compare the "System Information" table with your actual specs.
2. **Verify Recommendations**:
   - Machines with < 4GB RAM should see **Lightweight** recommendations (Puppy, AntiX).
   - Machines with NVIDIA GPUs should see **Pop!_OS** in the list.
   - Machines with SSDs will receive a higher performance score.
3. **Logs**: Check the terminal where `app.py` is running for any Flask errors or hardware detection warnings.

---

## � Project Structure

```text
linux-z/
├── backend/            # Core logic, analyzer, and Flask API
│   ├── analyzer.py     # Hardware detection logic
│   ├── scorer.py       # Recommendation engine
│   ├── distros.json    # Distro database
│   └── app.py          # Web Server
├── frontend/           # Web UI assets
│   ├── templates/      # HTML (Jinja2)
│   └── static/         # CSS and images
├── cli/                # Terminal interface
└── requirements.txt    # Project dependencies
```

---

## � License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve hardware detection or add new distros to the database.
