from Bio import SeqIO

record = SeqIO.read("rna.fasta", "fasta")
rna = record.seq.transcribe()

structure = "(((...)))"

stack = []
pairs = []

for i, ch in enumerate(structure):
    if ch == "(":
        stack.append(i + 1)
    elif ch == ")":
        if stack:
            start = stack.pop()
            pairs.append((start, i + 1))

print("RNA Sequence:")
print(rna)

print("Sequence Length:", len(rna))
print("Structure Length:", len(structure))

print("Base Pair Positions:")
print(pairs)