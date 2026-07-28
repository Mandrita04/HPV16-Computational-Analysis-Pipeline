from Bio import Entrez
Entrez.email = "mandrita670@gmail.com"
handle=Entrez.esearch(db="gene", term="E6[Gene Name] AND E7[Gene Name] AND Homo sapiens[Organism]")
search_results=Entrez.read(handle)
handle.close()
print("Search result for E6 and E7 genes:")
print(search_results)
