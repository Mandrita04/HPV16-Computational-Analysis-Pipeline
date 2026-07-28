from Bio.Blast import NCBIWWW

sequence = input("Enter protein sequence: ").strip()

print("Running BLAST... Please wait.")

result_handle = NCBIWWW.qblast(
    program="blastp",
    database="nr",
    sequence=sequence
)

with open("blast_result.xml", "w") as out_file:
    out_file.write(result_handle.read())

result_handle.close()

print("BLAST completed successfully.")
print("Results saved as blast_result.xml")