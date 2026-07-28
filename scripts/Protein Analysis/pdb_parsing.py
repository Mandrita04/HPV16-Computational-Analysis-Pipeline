from Bio.PDB import PDBParser

filename = input("Enter the PDB file name: ")

parser = PDBParser()

structure = parser.get_structure("Protein", filename)

print("Structure ID:", structure.id)

for model in structure:
    print("Model:", model.id)

    for chain in model:
        print("Chain:", chain.id)

        count = 0
        for residue in chain:
            count += 1

        print("Number of residues:", count)