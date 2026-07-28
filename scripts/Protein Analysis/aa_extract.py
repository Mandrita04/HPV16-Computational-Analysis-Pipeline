#Extract the amino acid sequence chainwise from a pdb file
from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1

filename = input("Enter PDB file: ")

parser = PDBParser(QUIET=True)
structure = parser.get_structure("Protein", filename)

sequence = ""

for model in structure:
    for chain in model:
        print("Chain:", chain.id)
        sequence = ""

        for residue in chain:
            if residue.id[0] == " ":      # Ignore water and hetero atoms
                sequence += seq1(residue.get_resname())

        print("Amino Acid Sequence:")
        print(sequence)