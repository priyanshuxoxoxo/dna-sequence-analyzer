# DNA FASTA Analyzer 2.0
# Beginner Bioinformatics Project

def read_fasta(filename):
    sequences = {}
    current_name = None

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                current_name = line[1:]
                sequences[current_name] = ""

            elif current_name is not None:
                sequences[current_name] += line.upper()

    return sequences


def analyze_dna(name, sequence):
    valid_bases = set("ATGC")

    if not sequence:
        print(f"\n{name}: Empty sequence. Skipping.")
        return

    if not set(sequence).issubset(valid_bases):
        print(f"\n{name}: Invalid DNA characters. Skipping.")
        return

    length = len(sequence)

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    gc_content = ((g + c) / length) * 100

    rna = sequence.replace("T", "U")

    complement_table = str.maketrans("ATGC", "TACG")
    reverse_complement = sequence.translate(complement_table)[::-1]

    print("\n" + "=" * 35)
    print("Sequence:", name)
    print("Length:", length, "bp")
    print("A:", a, " T:", t, " G:", g, " C:", c)
    print(f"GC Content: {gc_content:.2f}%")
    print("RNA Sequence:", rna)
    print("Reverse Complement:", reverse_complement)


def main():
    filename = "sample.fasta"

    try:
        sequences = read_fasta(filename)
    except FileNotFoundError:
        print(f"Error: {filename} was not found.")
        print("Keep sample.fasta in the same folder as this program.")
        return

    if not sequences:
        print("No sequences found in the FASTA file.")
        return

    print("DNA FASTA ANALYZER 2.0")
    print("Sequences found:", len(sequences))

    for name, sequence in sequences.items():
        analyze_dna(name, sequence)


if __name__ == "__main__":
    main()
