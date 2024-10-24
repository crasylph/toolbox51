#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
$DebugPreference = "Continue"


# # 导入 Conda 环境
# $CondaPath = "$env:USERPROFILE\miniconda3\etc\profile.d\conda.sh"
# & "$CondaPath" | Invoke-Expression

# # 激活 Conda 环境
# $CondaEnvPath = "$PWD\.conda"
# conda activate $CondaEnvPath

# 获取版本号

$ModulePath = $args[0]
if (-not $env:VERSION) {
    $Version = python -c "from $ModulePath import __version__; print(__version__)"
    $env:VERSION = $Version
}
Write-Output "Version: $env:VERSION"

# 处理版本号中的 dev
if ($env:VERSION -match 'dev$') {
    $env:VERSION = $env:VERSION -replace 'dev$', 'dev0'
}


# 设置 Wheel 名称
$WheelName = "$ModulePath-$env:VERSION-py3-none-any.whl"
Write-Output "Wheel Name: $WheelName"

# 检查 Wheel 文件是否存在
$WheelPath = "dist\$WheelName"
if (Test-Path -Path $WheelPath) {
    Write-Output "Warning: $WheelPath exists, skip building"
    exit 0
}

# 构建 Wheel
python -m pip wheel -w dist . --no-deps
