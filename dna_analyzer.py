
# DNA Sequence Analyzer
# First Bioinformatics Project by Priyanshu

from pathlib import Path


def analyze_dna(dna):
    # Convert to uppercase and remove spaces
    dna = "".join(dna.upper().split())

    # Check if the sequence is empty
    if not dna:
        print("Error: DNA sequence cannot be empty!")
        return

    # Check for invalid characters
    valid_bases = "ATGC"

    for base in dna:
        if base not in valid_bases:
            print("Error: Invalid DNA sequence!")
            print("Only A, T, G, and C are allowed.")
            return

    # Count each nucleotide
    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    # Calculate sequence length
    length = len(dna)

    # Calculate GC content
    gc_content = ((g + c) / length) * 100

    # Convert DNA to RNA
    rna = dna.replace("T", "U")

    # Generate reverse complement
    complement = ""

    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "T":
            complement += "A"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"

    reverse_complement = complement[::-1]

    # Display results
    print("\n========== DNA ANALYSIS ==========")
    print("DNA Sequence:", dna)
    print("Sequence Length:", length, "bp")

    print("\nNucleotide Count:")
    print("Adenine (A):", a)
    print("Thymine (T):", t)
    print("Guanine (G):", g)
    print("Cytosine (C):", c)

    print(f"\nGC Content: {gc_content:.2f}%")
    print("RNA Sequence:", rna)
    print("Reverse Complement:", reverse_complement)

    # Save results to a file
    report = f"""
DNA SEQUENCE ANALYSIS REPORT
============================

DNA Sequence: {dna}
Sequence Length: {length} bp

Nucleotide Count:
A: {a}
T: {t}
G: {g}
C: {c}

GC Content: {gc_content:.2f}%
RNA Sequence: {rna}
Reverse Complement: {reverse_complement}
"""

    Path("results.txt").write_text(report, encoding="utf-8")

    print("\nReport saved successfully as results.txt")


# Main program
print("================================")
print("    DNA SEQUENCE ANALYZER")
print("================================")

sequence = input("Enter your DNA sequence: ")

analyze_dna(sequence)


