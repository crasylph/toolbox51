#!/bin/bash
set -ex
source ~/miniconda3/etc/profile.d/conda.sh 
conda activate $PWD/.conda
python -m pip wheel -w dist . --no-deps