#Hairpin detection
structure = input("Enter the hairpin structure to detect")

if "(" in structure and ")" in structure and "..." in structure:
    print("Hairpin structure detected")
else:
    print("No hairpin detected")

