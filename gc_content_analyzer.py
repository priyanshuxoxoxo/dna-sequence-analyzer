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


def calculate_gc_content(sequence):
    sequence = sequence.upper()
    total = len(sequence)

    if total == 0:
        return 0

    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / total) * 100


def main():
    fasta_file = Path(__file__).with_name("sample.fasta")

    if not fasta_file.exists():
        print("Error: sample.fasta was not found.")
        return

    sequences = read_fasta(fasta_file)

    if not sequences:
        print("No DNA sequences found.")
        return

    names = []
    gc_values = []

    for name, sequence in sequences.items():
        if not sequence or set(sequence) - set("ATGC"):
            print(f"Skipping invalid sequence: {name}")
            continue

        gc = calculate_gc_content(sequence)

        names.append(name)
        gc_values.append(gc)

        print(f"{name}: GC content = {gc:.2f}%")

    if not names:
        print("No valid DNA sequences to analyze.")
        return

    plt.figure(figsize=(8, 5))
    plt.bar(names, gc_values)
    plt.axhline(y=50, linestyle="--", label="50% reference")
    plt.xlabel("DNA Sequence")
    plt.ylabel("GC Content (%)")
    plt.title("GC Content Comparison")
    plt.ylim(0, 100)
    plt.legend()
    plt.tight_layout()

    output = Path(__file__).with_name("gc_content_comparison.png")
    plt.savefig(output, dpi=300)

    print(f"\nGraph saved as {output.name}")
    plt.show()


if __name__ == "__main__":
    main()