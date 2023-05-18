#!/bin/bash
#$ -l tmem=3.9G
#$ -l h_vmem=3.9G
#$ -l h_rt=02:54:00
#$ -S /bin/bash
#$ -N src_active
#$ -t 1-2
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
which conda
conda deactivate
conda init bash
conda activate dockstring
cd /SAN/orengolab/nsp13/dude/cluster_dockstring
# UPDATE FOR YOUR ENVIRONMENT
which python
/SAN/orengolab/nsp13/.conda/envs/dockstring/bin/python batch_run_dockstring.py --task_index ${SGE_TASK_ID} --smiles_file dude_data/selected_dude/src/actives_final.ism --target SRC --active_decoy active
date
    