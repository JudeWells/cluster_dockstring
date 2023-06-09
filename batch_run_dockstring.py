import os
import time
import sys
import argparse
import shutil
sys.path.append('/SAN/orengolab/nsp13/dude/dockstring')

from dockstring import load_target

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Dock batch of ligands to a target."
    )
    parser.add_argument("--task_index", type=int)
    parser.add_argument("--target", type=str)
    parser.add_argument("--active_decoy", type=str)
    parser.add_argument("--smiles_file", type=str)
    args = parser.parse_args()
    batch_size = 300
    task_index = args.task_index - 1
    with open(args.smiles_file, "r") as f:
        smiles_lines = f.readlines()[task_index*batch_size:(task_index+1)*batch_size]
    for i, line in enumerate(smiles_lines):
        start = time.time()
        try:
            if args.active_decoy == "active":
                smiles, _, lig_id = line.split()
            else:
                smiles, lig_id = line.split()
            working_directory = f"/SAN/orengolab/nsp13/dude/outputs_dockstring/{args.target}/{args.active_decoy}/{task_index}/{lig_id}/"
            os.makedirs(working_directory, exist_ok=True)
            print(smiles)
            target = load_target(args.target, working_dir=working_directory)
            score, _ = target.dock(smiles)
            print(f"Docking was successful, score={score:.3g}. time={round(time.time()-start, 1)}s.")
            for fname in ['ligand.mol',  'vina.log', 'vina.out', 'ligand.pdbqt']:
                os.remove(os.path.join(working_directory, fname))
        except Exception as e:
            print(f"Docking failed with error: {e}")
            continue
    directory_path = f"/SAN/orengolab/nsp13/dude/outputs_dockstring/{args.target}/{args.active_decoy}/{task_index}/"
    shutil.make_archive(directory_path, 'zip', directory_path)
    shutil.rmtree(directory_path)
