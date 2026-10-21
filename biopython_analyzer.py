from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

print("=" * 40)
print("     BIOPYTHON DNA ANALYZER")
print("=" * 40)

dna = input("Enter a DNA sequence: ").upper().strip()

if not dna:
    print("Error: Sequence cannot be empty.")

elif any(base not in "ATGC" for base in dna):
    print("Invalid DNA sequence!")
    print("Only A, T, G, and C are allowed.")

else:
    sequence = Seq(dna)

    print("\n--- ANALYSIS RESULTS ---")
    print("DNA Sequence:", sequence)
    print("Sequence Length:", len(sequence))
    print("GC Content:", round(gc_fraction(sequence) * 100, 2), "%")
    print("RNA Sequence:", sequence.transcribe())
    print("Reverse Complement:", sequence.reverse_complement())

    complete_length = len(sequence) - len(sequence) % 3
    coding_sequence = sequence[:complete_length]

    if complete_length > 0:
        print("Protein Sequence:", coding_sequence.translate())
    else:
        print("Protein Sequence: Not enough bases for a complete codon.")

    if len(sequence) % 3 != 0:
        print("Note: The final incomplete codon was excluded.")

print("\nAnalysis complete!")