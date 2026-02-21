#!/bin/bash

# Linux Hardware Data Collection Script

# RAM in bytes
RAM=$(free -b | grep Mem | awk '{print $2}')

# CPU Cores
CPU_CORES=$(nproc)

# Architecture
ARCH=$(uname -m)

# Disk size in bytes (Root partition)
DISK=$(df -B1 / | tail -1 | awk '{print $2}')

# Processor Model
CPU_MODEL=$(lscpu | grep "Model name" | cut -d ':' -f 2 | xargs)

# Export to JSON
echo "{
  \"ram_bytes\": $RAM,
  \"cpu_cores\": $CPU_CORES,
  \"arch\": \"$ARCH\",
  \"disk_bytes\": $DISK,
  \"cpu_model\": \"$CPU_MODEL\"
}" > system_info.json
