def find_motif(sequence, motif):
    sequence = sequence.upper().strip()
    motif = motif.upper().strip()

    if not sequence:
        print("Error: DNA sequence cannot be empty.")
        return

    if not motif:
        print("Error: Motif cannot be empty.")
        return

    if set(sequence) - set("ATGC"):
        print("Error: DNA sequence contains invalid characters.")
        return

    if set(motif) - set("ATGC"):
        print("Error: Motif contains invalid characters.")
        return

    positions = []
    start = 0

    while True:
        position = sequence.find(motif, start)

        if position == -1:
            break

        positions.append(position + 1)
        start = position + 1

    print("\n=== DNA Motif Finder ===")
    print(f"DNA sequence: {sequence}")
    print(f"Motif searched: {motif}")
    print(f"Total occurrences: {len(positions)}")

    if positions:
        print("Positions (1-based):", positions)
    else:
        print("Motif not found.")


def main():
    print("Welcome to the DNA Motif Finder!")

    sequence = input("Enter your DNA sequence: ")
    motif = input("Enter the motif to search for: ")

    find_motif(sequence, motif)


if __name__ == "__main__":
    main()