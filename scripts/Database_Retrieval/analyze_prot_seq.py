from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

filename = input("Enter FASTA file path: ")

try:
    record = SeqIO.read(filename, "fasta")

    protein = str(record.seq).upper()

    analysis = ProteinAnalysis(protein)

    print("Protein ID:", record.id)
    print("Protein Length:", len(protein), "amino acids")
    print("Molecular Weight:", round(analysis.molecular_weight(), 2), "Da")
    print("Isoelectric Point:", round(analysis.isoelectric_point(), 2))
    print("Amino Acid Count:")
    print(analysis.count_amino_acids())

except FileNotFoundError:
    print("File not found.")

except Exception as e:
    print("Error:", e)