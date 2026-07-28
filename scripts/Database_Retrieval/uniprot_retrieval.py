# UniProt Retrieval to get protein information
from Bio import ExPASy
from Bio import SwissProt   
accession = input("Enter Uniprot Accession number for E6 or E7 gene:") 
with ExPASy.get_sprot_raw(accession) as handle: # Fetch the raw Swiss-Prot record for the specified accession number
  record = SwissProt.read(handle) # Read the Swiss-Prot record    
 
print(record) 
print(f"Protein Name: {record.description}")
print(f"Organism:     {record.organism}")
print(f"Sequence Len: {record.sequence_length} amino acids")
print(f"Sequence:     {record.sequence[:40]}...") 

with open("protein.fasta", "w") as file:#save the protein sequence in FASTA format
    file.write(record.sequence)
print("Protein sequence saved.")
#Analyze the protein sequence
print("Methionine count:", record.sequence.count("M"))# Count the number of methionine (M) residues in the protein sequence
print("Lysine count:", record.sequence.count("K"))# Count the number of lysine (K) residues in the protein sequence