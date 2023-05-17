import sys
import argparse
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
    batch_size = 100
    task_index = args.task_index - 1
    with open(args.smiles_file, "r") as f:
        smiles_lines = f.readlines()[task_index*batch_size:(task_index+1)*batch_size]
    for i, line in enumerate(smiles_lines):
        if args.active_decoy == "active":
            smiles, _, lig_id = line.split()
        else:
            smiles, lig_id = line.split()
        working_directory = f"/SAN/orengolab/nsp13/dude/outputs_dockstring/{args.target}/{args.active_decoy}/{lig_id}/"
        target = load_target(args.target, working_dir=working_directory)
        score, _ = target.dock(smiles)
        print(f"Docking was successful, score={score:.3g}. END OF SCRIPT.")
