#Visualize BLAST results using matplotlib
from Bio.Blast import NCBIXML
import matplotlib.pyplot as plt

with open("blast_result.xml") as result_handle:
    blast_record = NCBIXML.read(result_handle)

# Extract scores for visualization
scores = []# Initialize an empty list to store the scores
for alignment in blast_record.alignments:# Loop through each hit in the BLAST record
    hsp = alignment.hsps[0]# Extract the first high-scoring segment pair (HSP) for each alignment
    scores.append(hsp.score)# Append(push) the score of the HSP to the scores list

# Create histogram of scores
plt.hist(scores, bins=20, edgecolor='black')# Create a histogram of the scores with 20 bins and black edges for better visibility
plt.xlabel('BLAST Score')
plt.ylabel('Frequency')
plt.title('Distribution of BLAST Scores')
plt.show()