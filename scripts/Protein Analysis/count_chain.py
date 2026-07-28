#count chains 
from Bio.PDB import PDBParser

parser = PDBParser()
structure = parser.get_structure("Protein", "E7.pdb")

chain_count = 0

for model in structure:
    for chain in model:
        chain_count += 1

print("Number of chains:", chain_count)