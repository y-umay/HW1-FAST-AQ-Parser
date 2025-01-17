# write tests for parsers
import os
from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    current_dir = os.path.dirname(__file__)
    # test corrupted data
    bad_path = os.path.join(current_dir, "bad.fa")
    parser = FastaParser(bad_path)
    with pytest.raises(ValueError, match="0 lines"):  
        for _ in parser:
            pass
    # test blank data
    blank_path = os.path.join(current_dir, "blank.fa")
    parser = FastaParser(blank_path)
    with pytest.raises(ValueError, match="0 lines"):  
        for _ in parser:
            pass
    # test empty_line
    empty_line_path = os.path.join(current_dir, "empty_line.fa")
    parser = FastaParser(empty_line_path)
    with pytest.raises(ValueError, match="empty line"):  
        for _ in parser:
            pass


def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    current_dir = os.path.dirname(__file__)
    fastq_path = os.path.join(current_dir, "..", "data", "test.fq")
    parser = FastaParser(fastq_path)
    as_list = list(parser)
    assert len(as_list) > 0
    assert len(as_list[0]) == 2
    assert as_list[0][0] is None
    

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    current_dir = os.path.dirname(__file__)
    # test corrupted data
    bad_path = os.path.join(current_dir, "bad.fq")
    parser = FastqParser(bad_path)
    with pytest.raises(ValueError, match="0 lines"):  
        for _ in parser:
            pass
    # test blank data
    blank_path = os.path.join(current_dir, "blank.fq")
    parser = FastqParser(blank_path)
    with pytest.raises(ValueError, match="0 lines"):  
        for _ in parser:
            pass
    # test empty_line
    empty_line_path = os.path.join(current_dir, "empty_line.fq")
    parser = FastqParser(empty_line_path)
    with pytest.raises(ValueError, match="empty line"):  
        for _ in parser:
            pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    current_dir = os.path.dirname(__file__)
    fasta_path = os.path.join(current_dir, "..", "data", "test.fa")
    parser = FastqParser(fasta_path)
    as_list = list(parser)
    assert len(as_list) > 0
    assert len(as_list[0]) == 2
    assert as_list[0][0] is None