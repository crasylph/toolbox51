#!/bin/bash
set -ex
source ~/miniconda3/etc/profile.d/conda.sh 
conda activate $PWD/.conda
pip install -e .[all]