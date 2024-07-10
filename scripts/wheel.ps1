#!/usr/bin/env pwsh

# set -e
$ErrorActionPreference = "Stop"
# set -x
$DebugPreference = "Continue"

# # 加载conda初始化脚本
# . (Resolve-Path ~/miniconda3/etc/profile.d/conda.sh)

# # 激活conda环境
# conda activate ($PWD.Path + "\.conda")

python -m pip wheel -w dist . --no-deps