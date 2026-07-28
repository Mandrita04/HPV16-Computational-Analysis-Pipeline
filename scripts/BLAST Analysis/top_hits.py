#Extract top hits
from Bio.Blast import NCBIXML

with open("blast_result.xml") as result_handle:

    blast_record = NCBIXML.read(result_handle)

    count = 0

    for alignment in blast_record.alignments:#stats a loop over all matching seq(hits) found for query

        for hsp in alignment.hsps:#stats a loop over all high-scoring segment pairs (HSPs) for each hit

            print("Hit:", alignment.title)# prints the title of the hit sequence
            print("Score:", hsp.score)# prints the score of the HSP, which indicates the quality of the match
            print("E-value:", hsp.expect)# prints the E-value of the HSP, which indicates the statistical significance of the match
            print()

            count += 1

            if count == 5:
                break

        if count == 5:
            break