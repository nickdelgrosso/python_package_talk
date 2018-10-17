from genomics import complement_dna

def test_complement_dna():
    assert complement_dna('GGC') == 'GCC'

def test_complement_dna2():
    assert complement_dna('TTTGGC') == 'GCCAAA'