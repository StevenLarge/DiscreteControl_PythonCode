#!/bin/bash
#SBATCH --account=def-dsivak
#SBATCH --time=15:00:00
#SBATCH --job-name=Optimization_Full

source OptEnv/bin/activate
python OptimalProtocolGenerator_Full.py


