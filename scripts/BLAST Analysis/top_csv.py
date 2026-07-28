#Save top hits to a CSV file
from Bio.Blast import NCBIXML
import csv

with open("blast_result.xml") as result_handle:

    blast_record = NCBIXML.read(result_handle)

with open("top_hits.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["Hit", "Score", "E-value"])#writes the header row in the CSV file having three columns: "Hit", "Score", and "E-value".

    for alignment in blast_record.alignments[:10]:#limit the number of hits to the top 10

        hsp = alignment.hsps[0]#extract the first high-scoring segment pair (HSP) for each alignment, which represents the best match for that hit.

        writer.writerow([alignment.title,hsp.score, hsp.expect])#writes a row in the CSV file for each hit, including the title of the hit sequence, the score of the HSP, and the E-value of the HSP.

print("CSV saved.")