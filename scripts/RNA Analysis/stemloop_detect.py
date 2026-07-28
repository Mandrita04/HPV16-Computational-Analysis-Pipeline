#Stem loop prediction
structure = input("Enter the stem loop structure to be predicted")

left = structure.count("(")
right = structure.count(")")

if left == right and left > 0:
    print("Possible stem-loop structure")
else:
    print("No stem-loop found")