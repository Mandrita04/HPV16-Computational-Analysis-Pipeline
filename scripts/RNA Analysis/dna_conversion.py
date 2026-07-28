
from Bio.Seq import Seq

dna = Seq(input("Enter your DNA sequence: "))

print("RNA Sequence:")
print(dna.transcribe())

print("Reverse Complement")
print(dna.reverse_complement())