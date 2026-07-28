#Extract amino acid sequence(Converts the residues into a string of amino acids)

from Bio.PDB import PDBParser
from Bio.SeqUtils import seq1#imports a utility function used to convert protein sequences from 3-letter amino acid codes to 1-letter codes

parser = PDBParser()
structure = parser.get_structure("Protein", "E7.pdb")
c=0
sequence = ""

for model in structure:
    for chain in model:
        for residue in chain:

            if residue.id[0] == " ":
                sequence += seq1(residue.resname)#converts a single residue's 3-letter name into a 1-letter code and appends it to a growing sequence string.
                c+=1
print("Protein Sequence:")
print(sequence)
print ("Number of amino acid residues:", c)