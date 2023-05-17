import sys
sys.path.append('/SAN/orengolab/nsp13/dude/dockstring')

from dockstring import load_target

if __name__ == "__main__":
    batch_size = 100
    task_index = int(sys.argv[1]) -1
    smiles_file = sys.argv[2]
    target = sys.argv[3]
    active_decoy = sys.argv[4]
    with open(smiles_file, "r") as f:
        smiles_lines = f.readlines()[task_index*batch_size:(task_index+1)*batch_size]
    for i, line in enumerate(smiles_lines):
        if active_decoy == "active":
            smiles, _, lig_id = line.split()
        else:
            smiles, lig_id = line.split()
        working_directory = f"/SAN/orengolab/nsp13/dude/outputs_dockstring/{target}/{active_decoy}/{lig_id}/"
        target = load_target(target, working_dir=working_directory)
        score, _ = target.dock(smiles)
        print(f"Docking was successful, score={score:.3g}. END OF SCRIPT.")
