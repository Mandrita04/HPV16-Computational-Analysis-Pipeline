from Bio import SeqIO

# Read DNA sequences
e6 = str(SeqIO.read("E6.fasta", "fasta").seq)
e7 = str(SeqIO.read("E7.fasta", "fasta").seq)

# Count codons
e6_codons = {}
e7_codons = {}

for i in range(0, len(e6)-2, 3):
    codon = e6[i:i+3]
    e6_codons[codon] = e6_codons.get(codon, 0) + 1

for i in range(0, len(e7)-2, 3):
    codon = e7[i:i+3]
    e7_codons[codon] = e7_codons.get(codon, 0) + 1

total_e6 = sum(e6_codons.values())
total_e7 = sum(e7_codons.values())

print("Codon\tE6 Freq\tE7 Freq")

for codon in sorted(set(e6_codons) | set(e7_codons)):
    f1 = e6_codons.get(codon, 0) / total_e6
    f2 = e7_codons.get(codon, 0) / total_e7

    print(codon, "\t", round(f1, 3), "\t", round(f2, 3))

    if f1 < 0.15:
        print("  Rare in E6")

    if f2 < 0.15:
        print("  Rare in E7")