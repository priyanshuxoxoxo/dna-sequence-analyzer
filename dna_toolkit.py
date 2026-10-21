def validate_dna(sequence):
    sequence = "".join(sequence.split()).upper()

    if not sequence:
        return False

    return not (set(sequence) - set("ATGC"))


def analyze_sequence(sequence):
    sequence = "".join(sequence.split()).upper()

    if not validate_dna(sequence):
        print("Invalid DNA sequence!")
        return

    length = len(sequence)
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    gc = ((g + c) / length) * 100

    print("\n--- DNA Analysis Results ---")
    print(f"Length: {length} bp")
    print(f"A: {a}")
    print(f"T: {t}")
    print(f"G: {g}")
    print(f"C: {c}")
    print(f"GC Content: {gc:.2f}%")
    print(f"RNA Sequence: {sequence.replace('T', 'U')}")


def find_motif(sequence, motif):
    sequence = "".join(sequence.split()).upper()
    motif = "".join(motif.split()).upper()

    if not validate_dna(sequence) or not validate_dna(motif):
        print("Invalid DNA sequence or motif!")
        return

    positions = []
    start = 0

    while True:
        position = sequence.find(motif, start)

        if position == -1:
            break

        positions.append(position + 1)
        start = position + 1

    print(f"\nMotif: {motif}")
    print(f"Occurrences: {len(positions)}")

    if positions:
        print(f"Positions (1-based): {positions}")
    else:
        print("Motif not found.")


def main():
    while True:
        print("\n====================================")
        print("       DNA ANALYSIS TOOLKIT")
        print("====================================")
        print("1. Analyze DNA sequence")
        print("2. Calculate GC content")
        print("3. Find DNA motif")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            sequence = input("Enter DNA sequence: ")
            analyze_sequence(sequence)

        elif choice == "2":
            sequence = input("Enter DNA sequence: ")

            if validate_dna(sequence):
                sequence = "".join(sequence.split()).upper()
                gc = (
                    (sequence.count("G") + sequence.count("C"))
                    / len(sequence)
                ) * 100

                print(f"GC Content: {gc:.2f}%")
            else:
                print("Invalid DNA sequence!")

        elif choice == "3":
            sequence = input("Enter DNA sequence: ")
            motif = input("Enter motif to search for: ")
            find_motif(sequence, motif)

        elif choice == "4":
            print("Thank you for using DNA Analysis Toolkit!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()