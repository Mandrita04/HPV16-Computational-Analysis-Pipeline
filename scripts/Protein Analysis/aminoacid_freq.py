#count amino acid residues
from Bio.PDB import PDBParser
from Bio.PDB.Polypeptide import is_aa #sub module handling protein chains and sequence conversions
filename = input("Enter the PDB file name: ")
parser = PDBParser()
structure = parser.get_structure("Protein", filename)

count = 0

for model in structure:
    for chain in model:
        for residue in chain:
            if is_aa(residue):#counts only the amino acids coding for protein
                count += 1

print("Amino acid residues:", count)