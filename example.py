import os
from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # File paths
    current_dir = os.path.dirname(__file__)
    fasta_file = os.path.join(current_dir, "data", "test.fa")
    fastq_file = os.path.join(current_dir, "data", "test.fq")

    # Create instance of FastaParser
    fasta_parser = FastaParser(fasta_file)

    # Create instance of FastqParser
    fastq_parser = FastqParser(fastq_file)
    
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print("\nProcessing FASTA Records for Transcribe:")
    for seq_name, sequence in fasta_parser:
        print(f"Header: {seq_name}")
        print(f"Original: {sequence}")
        print(f"Transcribed: {transcribe(sequence)}")
        print("#" * 40)

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print("\n\n\nProcessing FASTQ Records for Transcribe & Reverse Transcribe:")
    for seq_name, sequence, _ in fastq_parser:
        print(f"Header: {seq_name}")
        print(f"Transcribed: {transcribe(sequence)}")
        print("*" * 40)

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print("\nProcessing FASTA Records for Reverse Transcribe:")
    for seq_name, sequence in fasta_parser:
        print(f"Header: {seq_name}")
        print(f"Original: {sequence}")
        print(f"Reverse Transcribed: {reverse_transcribe(sequence)}")
        print("#" * 40)
    
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print("\n\n\nProcessing FASTQ Records for Reverse Transcribe:")
    for seq_name, sequence, _ in fastq_parser:
        print(f"Header: {seq_name}")
        print(f"Reverse Transcribed: {reverse_transcribe(sequence)}")
        print("*" * 40)



"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
