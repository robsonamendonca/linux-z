# 📌 1. Objetivo do Projeto

Desenvolver um sistema offline capaz de:

1. Identificar propriedades do hardware:

   * Memória RAM total
   * Espaço total e livre em disco
   * Arquitetura (32 ou 64 bits)
   * Número de núcleos da CPU
   * Modelo do processador
2. Gerar uma **nota de performance**
3. Classificar o perfil do equipamento (baixo, médio, alto desempenho)
4. Sugerir a melhor distribuição Linux adequada ao hardware

---

# 📌 2. Arquitetura do Projeto

Estrutura modular recomendada:

```
offline/
│
├── linux/
│   ├── collect.sh
│
├── windows/
│   ├── collect.cmd
│   ├── collect.ps1
│
├── macos/
│   ├── collect.sh
│
├── core/
│   ├── scorer.py
│   ├── recommender.py
│   └── profiles.json
│
└── main.py
```

---

# 📌 3. Estratégia Técnica (Offline)

Como não podemos usar bibliotecas Python externas como `psutil`, utilizaremos:

* Comandos nativos do SO
* Redirecionamento de saída para arquivos `.json` ou `.txt`
* Parsing usando apenas bibliotecas padrão do Python:

  * `os`
  * `subprocess`
  * `platform`
  * `json`
  * `re`

---

# 📌 4. Coleta de Dados por Sistema

---

# 🐧 Linux (Shell Script)

![Image](https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/Linux_command-line._Bash._GNOME_Terminal._screenshot.png/960px-Linux_command-line._Bash._GNOME_Terminal._screenshot.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2ANyY7NF_dtaKkptmf9J6BYQ.png)

![Image](https://i.sstatic.net/Ak1Ts.png)

![Image](https://www.howtoforge.com/images/command-tutorial/lscpu.png)

### Script: `collect.sh`

Comandos necessários:

### 🔹 Memória RAM

```bash
free -b | grep Mem
```

### 🔹 Arquitetura

```bash
uname -m
```

### 🔹 CPU

```bash
lscpu
```

### 🔹 Disco

```bash
df -B1 /
```

### 🔹 Núcleos

```bash
nproc
```

### Saída recomendada:

Gerar um JSON:

```bash
echo "{
  \"ram_bytes\": $RAM,
  \"disk_bytes\": $DISK,
  \"arch\": \"$ARCH\",
  \"cpu_cores\": $CORES
}" > system_info.json
```

---

# 🪟 Windows

## 🔹 Opção 1: PowerShell (Preferencial)

![Image](https://redmondmag.com/articles/2015/01/23/~/media/ECG/redmondmag/Images/2015/01/PowerShellInfo_Fig2.ashx)

![Image](https://images.ctfassets.net/xwxknivhjv1b/4jXPlj7aLBqQqWGb5zoQRq/5bdfd32fb4fe54978ea6b4463979b97c/cimwmi3.png?fl=png8\&fm=png\&h=750\&q=80\&w=1000)

![Image](https://habrastorage.org/getpro/habr/post_images/7d6/6d2/a5e/7d66d2a5e49ef9e909f7a45403bd44d4.jpg)

![Image](https://habrastorage.org/getpro/habr/post_images/c08/18d/d39/c0818dd39edc80cfce59e924f17b9457.jpg)

### Script: `collect.ps1`

### RAM

```powershell
(Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory
```

### CPU

```powershell
(Get-CimInstance Win32_Processor).NumberOfCores
```

### Arquitetura

```powershell
(Get-CimInstance Win32_OperatingSystem).OSArchitecture
```

### Disco

```powershell
(Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'").Size
```

Exportar para JSON:

```powershell
$data | ConvertTo-Json | Out-File system_info.json
```

---

## 🔹 Opção 2: CMD (Fallback)

```cmd
systeminfo
wmic cpu get NumberOfCores
wmic OS get OSArchitecture
```

Parsing feito no Python.

---

# 🍎 macOS

![Image](https://iboysoft.com/images/en-wiki/mac-system-profiler/retrieve-system-information-via-terminal-mac.png)

![Image](https://i.sstatic.net/A28ze.png)

![Image](https://discussions.apple.com/content/attachment/120368040)

![Image](https://imgv2-2-f.scribdassets.com/img/document/2084227/original/ee9c6e340b/1?v=1)

### Script: `collect.sh`

### RAM

```bash
sysctl -n hw.memsize
```

### CPU cores

```bash
sysctl -n hw.ncpu
```

### Arquitetura

```bash
uname -m
```

### Disco

```bash
df -k /
```

Exportar para JSON semelhante ao Linux.

---

# 📌 5. Engine de Pontuação (scorer.py)

Critérios objetivos:

| Critério    | Peso |
| ----------- | ---- |
| RAM         | 40%  |
| CPU         | 30%  |
| Disco       | 20%  |
| Arquitetura | 10%  |

### Exemplo de regra:

#### RAM

* < 2GB → 10 pts
* 2–4GB → 30 pts
* 4–8GB → 60 pts
* > 8GB → 100 pts

#### CPU cores

* 1 core → 20 pts
* 2 cores → 40 pts
* 4 cores → 70 pts
* > 4 cores → 100 pts

Nota final:

```python
score = (ram_score * 0.4) + (cpu_score * 0.3) + (disk_score * 0.2) + (arch_score * 0.1)
```

Classificação:

* 0–40 → Low-end
* 41–70 → Mid-range
* 71–100 → High-end

---

# 📌 6. Motor de Recomendação (recommender.py)

Arquivo `profiles.json`:

```json
{
  "low": ["Lubuntu", "Linux Lite", "antiX"],
  "mid": ["Linux Mint XFCE", "Ubuntu MATE"],
  "high": ["Ubuntu", "Fedora Workstation", "Pop!_OS"]
}
```

Regras:

* Se arquitetura for 32 bits → priorizar versões legacy
* Se RAM < 4GB → priorizar XFCE ou LXDE
* Se > 8GB → sugerir GNOME ou KDE

---

# 📌 7. Fluxo do Sistema

```
1. Detecta SO via platform.system()
2. Executa script nativo correspondente
3. Gera system_info.json
4. scorer.py calcula nota
5. recommender.py sugere distro
6. Exibe resultado final
```

---

# 📌 8. Resultado Final Esperado

Exemplo de saída:

```
Sistema analisado:
RAM: 4GB
CPU: 2 cores
Arquitetura: 64 bits
Disco: 256GB

Nota de performance: 58/100
Perfil: Intermediário

Distribuições recomendadas:
- Linux Mint XFCE
- Ubuntu MATE
```

---

# 📌 9. Considerações Técnicas Importantes

### 🔹 Compatibilidade

* Garantir fallback se comando não existir
* Validar parsing

### 🔹 Segurança

* Não executar comandos com entrada do usuário
* Scripts apenas leitura de sistema

### 🔹 Portabilidade

* Usar apenas ferramentas nativas
* Nenhuma dependência externa

---

# 📌 10. Próximas Evoluções Futuras

* Interface CLI amigável
* Interface gráfica Tkinter (offline)
* Versão compilada com PyInstaller
* Exportação de relatório PDF offline
* Benchmark sintético local (CPU test simples)

---

# 📌 Conclusão

Este projeto é totalmente viável offline utilizando:

* Shell scripting
* PowerShell
* CMD
* Python padrão

Ele mantém:

* Zero dependências externas
* Total portabilidade
* Baixo risco de falha
* Execução em qualquer ambiente sem internet

