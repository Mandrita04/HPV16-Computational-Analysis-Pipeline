#Predict RNA Secondary structure using ViennaRNA
import RNA#provides tools for RNA secondary structure prediction and related analyses

sequence = input("Enter the RNA sequence to predict its secondary structure: ")

structure, mfe = RNA.fold(sequence)
#RNA.fold(sequence): Executes the core RNAfold prediction logic on your input string.
#structure: Receives the calculated configuration in standard dot-bracket notation.
#mfe: Receives a float tracking the calculated Minimum Free Energy in kcal/mol.
print("Sequence :", sequence)
print("Structure:", structure)
print("MFE:", mfe)