#!/bin/bash
set -ex
source ~/miniconda3/etc/profile.d/conda.sh 
conda activate $PWD/.conda
langchain serve --host=0.0.0.0 --port=50010