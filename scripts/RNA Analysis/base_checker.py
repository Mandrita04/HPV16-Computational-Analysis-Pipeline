seq1 = input("Enter first RNA sequence: ").upper()
seq2 = input("Enter second RNA sequence: ").upper()

pairs = {"A": "U", "U": "A", "G": "C", "C": "G"}

if len(seq1) != len(seq2):
    print("Sequences must be of the same length.")
else:
    correct = True

    for i in range(len(seq1)):
        if pairs[seq1[i]] != seq2[i]:
            correct = False
            break

    if correct:
        print("Perfect RNA base pairing.")
    else:
        print("Not a valid RNA base pairing.")
        