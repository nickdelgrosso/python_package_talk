from genomics import complement_dna
import pytest

@pytest.mark.parametrize('seq,comp', [('GGC', 'GCC'), ('TTTGGC', 'GCCAAA')])
def test_complement_dna(seq, comp):
    assert complement_dna(seq) == comp

