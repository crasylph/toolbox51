#!/bin/bash

source ~/miniconda3/etc/profile.d/conda.sh 
conda activate $PWD/.conda


if [ -z "$VERSION" ]; then
    VERSION=$(python -c "from $1 import __version__; print(__version__)")
fi
if [[ $VERSION == *dev ]]; then
    VERSION="${VERSION/dev/dev0}"
fi

WHEEL_NAME="$1-$VERSION-py3-none-any.whl"

if [ -f "dist/$WHEEL_NAME" ]; then
    echo "Warning: "dist/$WHEEL_NAME"已存在，跳过构建"
    exit 0
fi

python -m pip wheel -w dist . --no-deps