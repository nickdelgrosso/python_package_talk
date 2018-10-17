
def get_dna_sequence():
    """
    Returns a DNA sequence.

    Returns: dna (str)
    """
    return 'GCCCTTTGTAAAG'


def complement_dna(seq):
    """
    Returns the reverse complement of the DNA sequence 'seq'.

    Args:
        seq (str): a DNA sequence

    Returns: comp_seq (str)

    Examples:
        >>> complement_dna('GGC')
        'GCC'

        >>> complement_dna('TTTGGC')
        'GCCAAA'
    """
    comp_seq = []
    for nt in seq:
        if nt == 'G':
            rnt = 'C'
        elif nt == 'C':
            rnt = 'G'
        elif nt == 'T':
            rnt = 'A'
        elif nt == 'A':
            rnt = 'T'
        comp_seq.append(rnt)

    comp_seq = ''.join(comp_seq)
    return comp_seq[::-1]


def transcribe_dna(seq):
    pass


def has_start_codon(rna_seq):
    pass


import doctest
doctest.testmod()