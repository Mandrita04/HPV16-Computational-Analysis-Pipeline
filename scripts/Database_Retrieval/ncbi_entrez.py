from Bio import Entrez
Entrez.email = "mandrita670@gmail.com"
accession = "NC_001526" # Example accession number for the TP53 gene
handle = Entrez.efetch(db="nucleotide", id=accession, rettype="gb", retmode="text")# Fetch the GenBank record for the specified accession number
seq=handle.read()# Read the content of the GenBank record
handle.close()# Close the handle after reading
print(seq)
with open("NCBIEntrez.fasta", "w") as file:# Open a file in write mode to save the sequence data
    file.write(seq)