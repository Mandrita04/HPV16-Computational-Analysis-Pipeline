from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

# Input FASTA file
filename = input("Enter protein FASTA file: ")

# Read protein sequence
record = SeqIO.read(filename, "fasta")
sequence = str(record.seq)

# Analyze protein
analysis = ProteinAnalysis(sequence)

print("Protein ID:", record.id)
print("Sequence Length:", len(sequence), "amino acids")
print("Molecular Weight:", round(analysis.molecular_weight(), 2), "Da")
print("Isoelectric Point (pI):", round(analysis.isoelectric_point(), 2))
print("GRAVY Score:", round(analysis.gravy(), 2))
print("Instability Index:", round(analysis.instability_index(), 2))
print("Aromaticity:", round(analysis.aromaticity(), 3))