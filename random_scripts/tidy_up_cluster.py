import os
import shutil
from random_scripts.generate_submit_scripts import get_last_task_index
batch_size = 300
targets = ["drd3", "esr1", "esr2", 'egfr', 'gcr', 'src']
for target in targets:
    for ac in ["active", "decoy"]:
        smiles_file = f"dude_data/selected_dude/{target.lower()}/{ac}s_final.ism"
        for task_index in range(0, get_last_task_index(target, ac)+1):
            new_working_directory = f"/SAN/orengolab/nsp13/dude/outputs_dockstring/{target}/{ac}/{task_index}/"
            os.makedirs(new_working_directory, exist_ok=True)
            with open(smiles_file, "r") as f:
                smiles_lines = f.readlines()[task_index * batch_size:(task_index + 1) * batch_size]
                print("loaded smiles file")
                for i, line in enumerate(smiles_lines):
                    if ac == "active":
                        smiles, _, lig_id = line.split()
                    else:
                        smiles, lig_id = line.split()
                    old_working_directory = f"/SAN/orengolab/nsp13/dude/outputs_dockstring/{target}/{ac}/{lig_id}"

                    for fname in ['ligand.mol', 'vina.log', 'vina.out', 'ligand.pdbqt']:
                        try:
                            os.remove(os.path.join(old_working_directory, fname))
                        except FileNotFoundError:
                            pass
                    shutil.move(old_working_directory, new_working_directory)
                print("moved this many files:", len(os.listdir(new_working_directory)))
                shutil.make_archive(new_working_directory, 'zip', new_working_directory)
                shutil.rmtree(new_working_directory)
