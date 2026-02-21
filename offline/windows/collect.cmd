@echo off
REM Windows Hardware Data Collection Script (CMD Fallback)
REM This is less ideal than PowerShell but provided as a backup.

echo Collecting data...
wmic ComputerSystem get TotalPhysicalMemory /value > temp_info.txt
wmic cpu get NumberOfCores /value >> temp_info.txt
wmic OS get OSArchitecture /value >> temp_info.txt
wmic LogicalDisk where "DeviceID='C:'" get Size /value >> temp_info.txt
wmic cpu get Name /value >> temp_info.txt

echo Data collected in temp_info.txt. Python will parse this.
