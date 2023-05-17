"""
Created by Jude Wells 2023-05-17
This script creates the txt file
which contains the smiles string
and the target to dock against
have 5 submission scripts each one
with a different target. Each one
has a list of smiles strings.
"""

targets = [
    "drd3", "esr1", "esr2", 'egfr', 'gcr', 'src'
]

def write_submit_script(target):
    n_ligands =
