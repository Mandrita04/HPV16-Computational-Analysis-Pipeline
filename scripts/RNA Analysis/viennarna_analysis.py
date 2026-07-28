#Predict Hairpins and Stem-Loops Using ViennaRNA
import RNA

sequence = input("Enter the Vienna RNA sequence to predict its secondary structure: ")

structure, mfe = RNA.fold(sequence)

print("Predicted Structure:")
print(structure)

if "(" in structure and ")" in structure:
    print("Stem-loop/Hairpin detected")

print("Minimum Free Energy:", mfe)