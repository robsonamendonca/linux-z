# Windows Hardware Data Collection Script (PowerShell)

$ram = (Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory
$cpuCores = (Get-CimInstance Win32_Processor).NumberOfCores
$arch = (Get-CimInstance Win32_OperatingSystem).OSArchitecture
$disk = (Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'").Size
$cpuModel = (Get-CimInstance Win32_Processor).Name

$data = @{
    ram_bytes  = [long]$ram
    cpu_cores  = [int]$cpuCores
    arch       = $arch
    disk_bytes = [long]$disk
    cpu_model  = $cpuModel
}

$data | ConvertTo-Json | Set-Content -Path "system_info.json" -Encoding utf8
