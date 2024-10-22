#!/usr/bin/env pwsh
$ErrorActionPreference = "Stop"
$DebugPreference = "Continue"

# 从 Python 模块中读取版本号
# $versionFile = Join-Path "src" "toolbox51" "__init__.py"
# $versionFile = "src/toolbox51/__init__.py"
# $version = (Get-Content $versionFile | Select-String '__version__').Matches[0].Groups[1].Value

# 根据版本号构建文件路径
# $whlFile = "dist/toolbox51-$version-py3-none-any.whl"
$whlFile = "dist/toolbox51-0.0.1.dev16-py3-none-any.whl"
# Write-Host $version

# # 检查文件是否存在
# if (-not (Test-Path $whlFile)) {
#     Write-Error "找不到文件: $whlFile"
#     exit 1
# }

# 上传到PyPI
twine upload $whlFile
