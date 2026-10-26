from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqUtils import gc_fraction

fasta_file = "sample.fasta"
output_file = "protein_results.txt"

print("=" * 45)
print("       FASTA PROTEIN ANALYZER")
print("=" * 45)

try:
    with open(output_file, "w") as report:
        for record in SeqIO.parse(fasta_file, "fasta"):
            dna = str(record.seq).upper()

            print(f"\nSequence ID: {record.id}")

            if not dna:
                print("Error: Empty sequence.")
                continue

            if any(base not in "ATGC" for base in dna):
                print("Skipped: Sequence contains non-ATGC characters.")
                continue

            sequence = Seq(dna)
            complete_length = len(sequence) - len(sequence) % 3
            coding_sequence = sequence[:complete_length]

            protein = coding_sequence.translate()

            result = (
                f"Sequence ID: {record.id}\n"
                f"DNA Length: {len(sequence)} bases\n"
                f"GC Content: {gc_fraction(sequence) * 100:.2f}%\n"
                f"Protein Length: {len(protein)} amino acids\n"
                f"Protein Sequence: {protein}\n"
                f"{'-' * 40}\n"
            )

            print(result)
            report.write(result)

    print(f"\nResults saved to {output_file}")

except FileNotFoundError:
    print(f"Error: {fasta_file} was not found.")
    print("Place sample.fasta in your project folder.")
