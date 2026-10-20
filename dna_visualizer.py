from pathlib import Path
import matplotlib.pyplot as plt


def read_fasta(filename):
    sequences = {}
    current_name = None

    with open(filename, "r", encoding="utf-8") as file:
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


def main():
    filename = Path(__file__).with_name("sample.fasta")

    if not filename.exists():
        print("Error: sample.fasta was not found.")
        return

    sequences = read_fasta(filename)

    if not sequences:
        print("No sequences found in the FASTA file.")
        return

    names = []
    a_counts = []
    t_counts = []
    g_counts = []
    c_counts = []

    for name, sequence in sequences.items():
        if not sequence or set(sequence) - set("ATGC"):
            print(f"Skipping invalid sequence: {name}")
            continue

        names.append(name)
        a_counts.append(sequence.count("A"))
        t_counts.append(sequence.count("T"))
        g_counts.append(sequence.count("G"))
        c_counts.append(sequence.count("C"))

    if not names:
        print("No valid DNA sequences to plot.")
        return

    positions = list(range(len(names)))
    width = 0.2

    plt.figure(figsize=(10, 6))
    plt.bar([p - 1.5 * width for p in positions], a_counts, width, label="A")
    plt.bar([p - 0.5 * width for p in positions], t_counts, width, label="T")
    plt.bar([p + 0.5 * width for p in positions], g_counts, width, label="G")
    plt.bar([p + 1.5 * width for p in positions], c_counts, width, label="C")

    plt.xticks(positions, names, rotation=15)
    plt.xlabel("DNA Sequence")
    plt.ylabel("Number of Nucleotides")
    plt.title("DNA Nucleotide Composition")
    plt.legend()
    plt.tight_layout()

    output = Path(__file__).with_name("dna_composition.png")
    plt.savefig(output, dpi=300)
    print("Graph saved to:", output.name)
    plt.show()


if __name__ == "__main__":
    main()