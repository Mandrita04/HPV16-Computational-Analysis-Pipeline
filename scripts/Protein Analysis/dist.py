#Computes the distance (Ångstroms) between the alpha-carbon atoms of two residues.
from Bio.PDB import PDBParser

parser = PDBParser()
structure = parser.get_structure("Protein", "E6.pdb")

chain = structure[0]["A"]#select the first model(Model 0) and the chain A
n1=input("Enter the 1st position")
n2=input("Enter the 2nd position")

res1 = chain[n1]#pick up the residue at nth position
res2 = chain[n2]

distance = res1["CA"] - res2["CA"]#isolate alpha carbon of both residue and calculate distance betwn them

print("Distance =", round(distance, 2), "Å")