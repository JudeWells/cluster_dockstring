#!/bin/bash
#$ -l tmem=3.9G
#$ -l h_vmem=3.9G
#$ -l h_rt=00:54:00
#$ -S /bin/bash
#$ -N dude
#$ -t 1-5
#$ -wd /SAN/orengolab/nsp13/dude/cluster_dockstring
# EXAMPLE SUBMISSION COMMAND:
# qsub /SAN/orengolab/nsp13/dude/cluster_dockstring/submit_scripts/dockstring.qsub.sh
#These are optional flags but you probably want them in all jobs
#$ -j y

echo "$@"
# args_file=$1
# entrypoint=$2
extra_args="${@:2}"  # e.g. batch size

hostname
date
conda activate dockstring
cd /SAN/orengolab/nsp13/dude/cluster_dockstring
# UPDATE FOR YOUR ENVIRONMENT
/SAN/orengolab/nsp13/.conda/envs/dockstring/bin/python vina_dock_ligand.py --task_index ${SGE_TASK_ID} --smiles_file dude_data/selected_dude/drd3/actives_final.ism --target drd3 --active_decoy active
date