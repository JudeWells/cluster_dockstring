import inspect

def get_last_task_index(target, active_decoy):
    with open(f'dude_data/selected_dude/{target.lower()}/{active_decoy}s_final.ism', 'r') as f:
        lines = f.readlines()
    return len(lines) // 300 + 1

def write_submit_script(target):
    for active_decoy in ['active', 'decoy']:
        filename = f'submit_scripts/{target}_{active_decoy}.qsub.sh'
        last_task_index = get_last_task_index(target, active_decoy)
        with open(filename, 'w') as outfile:
            outfile.write(inspect.cleandoc(f'''
#!/bin/bash
#$ -l tmem=3.9G
#$ -l h_vmem=3.9G
#$ -l h_rt=02:54:00
#$ -S /bin/bash
#$ -N {target}_{active_decoy}
#$ -t 1-{last_task_index}
#$ -wd /SAN/orengolab/nsp13/dude/cluster_dockstring
# EXAMPLE SUBMISSION COMMAND:
# qsub /SAN/orengolab/nsp13/dude/cluster_dockstring/submit_scripts/dockstring.qsub.sh
#These are optional flags but you probably want them in all jobs
#$ -j y

echo "$@"
# args_file=$1
# entrypoint=$2
extra_args="${{@:2}}"  # e.g. batch size

hostname
date
which conda
conda deactivate
conda init bash
conda activate dockstring
cd /SAN/orengolab/nsp13/dude/cluster_dockstring
# UPDATE FOR YOUR ENVIRONMENT
which python
/SAN/orengolab/nsp13/.conda/envs/dockstring/bin/python batch_run_dockstring.py --task_index ${{SGE_TASK_ID}} --smiles_file dude_data/selected_dude/{target.lower()}/{active_decoy}s_final.ism --target {target.upper()} --active_decoy {active_decoy}
date
    '''))

if __name__ == '__main__':
    targets = ["drd3", "esr1", "esr2", 'egfr', 'gcr', 'src']
    for target in targets:
        write_submit_script(target)