#!/bin/bash
#SBATCH --account=def-dsivak
#SBATCH --mem=1000M
#SBATCH --time=15:00:00
#SBATCH --job-name=Opt_Full_12_15

source OptEnv/bin/activate
python OptimalProtocolGenerator_Full_12_15.py


