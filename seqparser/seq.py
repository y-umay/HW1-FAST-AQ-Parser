# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    # Convert the sequence to uppercase
    seq = seq.upper()

    # Validate the sequence
    for base in seq:
        if base not in ALLOWED_NUC:
            raise ValueError("Sequence contains invalid character.")
    
    #Transcribe the sequence
    transcribed = []
    for base in seq:
        transcribed.append(TRANSCRIPTION_MAPPING[base])
    transcribed = ''.join(transcribed)
    
    #Reverse the sequence, if needed
    if reverse:
        transcribed = transcribed[::-1]
    return transcribed

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    return transcribe(seq, reverse=True)