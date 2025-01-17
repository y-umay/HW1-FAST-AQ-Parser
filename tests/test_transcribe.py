# write tests for transcribe functions
import pytest
from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    #test the input
    seq="ACTXGGT"
    with pytest.raises(ValueError, match="invalid character"):
        transcribe(seq)
    #test transcribe function
    assert transcribe("ACTGAACCC") == "UGACUUGGG"
    #test if handles lowercase
    assert transcribe("actgaaccc") == "UGACUUGGG"
    # Test reverse transcripte mode
    assert transcribe("ACTGAACCC", reverse=True) == "GGGUUCAGU"


def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    # Test reverse transcription
    assert reverse_transcribe("ACTGAACCC") == "GGGUUCAGU"
    # Test if handles lowercase input
    assert reverse_transcribe("actgaaccc") == "GGGUUCAGU"