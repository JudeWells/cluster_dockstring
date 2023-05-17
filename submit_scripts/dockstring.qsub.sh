#!/bin/bash
#$ -l tmem=3.9G
#$ -l h_vmem=3.9G
#$ -l h_rt=01:55:30
#$ -S /bin/bash
#$ -N docking
#$ -t 1-192
#$ -wd /SAN/orengolab/nsp13/dock_pdbbind/random_scripts
# EXAMPLE SUBMISSION COMMAND:
#These are optional flags but you probably want them in all jobs
#$ -j y
hostname
date
PROJECT_HOME=/SAN/orengolab/nsp13/shared
source $PROJECT_HOME/source_files/vina.source
source $PROJECT_HOME/source_files/conda.source
conda activate cheminfo2
cd /SAN/orengolab/nsp13/dock_pdbbind/random_scripts
# UPDATE FOR YOUR ENVIRONMENT
/SAN/orengolab/nsp13/.conda/envs/cheminfo2/bin/python3 vina_dock_ligand.py ${SGE_TASK_ID}
date