#Protein motif search
from Bio import SeqIO
sequence= input("Enter amino acid sequence")


motif = "KLV"

for i in range(len(sequence) - len(motif) + 1):
    if sequence[i:i+len(motif)] == motif:
        print("Motif found at position", i + 1)