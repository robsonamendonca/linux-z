#!/bin/bash

# macOS Hardware Data Collection Script

# RAM in bytes
RAM=$(sysctl -n hw.memsize)

# CPU Cores
CPU_CORES=$(sysctl -n hw.ncpu)

# Architecture
ARCH=$(uname -m)

# Disk size in bytes (Root partition)
# df -k / returns values in 1024-byte blocks
DISK_KB=$(df -k / | tail -1 | awk '{print $2}')
DISK=$((DISK_KB * 1024))

# Processor Model
CPU_MODEL=$(sysctl -n machdep.cpu.brand_string)

# Export to JSON
echo "{
  \"ram_bytes\": $RAM,
  \"cpu_cores\": $CPU_CORES,
  \"arch\": \"$ARCH\",
  \"disk_bytes\": $DISK,
  \"cpu_model\": \"$CPU_MODEL\"
}" > system_info.json
