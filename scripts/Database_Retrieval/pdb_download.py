from Bio.PDB import PDBList
pdb_id = input("Enter the PDB ID(E6 or E7):") 
pdb = PDBList()
pdb.retrieve_pdb_file(pdb_id,pdir=".",file_format="pdb")# Download the PDB structure file for the specified PDB ID and save it in the current directory
print(f"PDB structure for {pdb_id} downloaded successfully.")