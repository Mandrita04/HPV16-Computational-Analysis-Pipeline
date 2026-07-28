from Bio import Entrez
Entrez.email = "mandrita670@gmail.com"
gene_id= ["E1", "E2", "E4", "E5", "E6", "E7"]
fetch = Entrez.efetch(
        db="gene",
        id=gene_id,
        retmode="xml"
)

record = Entrez.read(fetch)
fetch.close()

gene_record = record[0]

# Gene symbol
symbol = gene_record["Entrezgene_gene"]["Gene-ref"]["Gene-ref_locus"]

    # Description
description = gene_record["Entrezgene_gene"]["Gene-ref"].get(
        "Gene-ref_desc", "Not available"
    )

    # Summary
summary = gene_record.get(
        "Entrezgene_summary",
        "Summary not available."
    )

print("Gene ID :", gene_id)
print("Symbol  :", symbol)
print("Description :", description)
print("\nSummary:")
print(summary)

print("\nDone!")