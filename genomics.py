
complement_nts = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}

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
    return ''.join(complement_nts[nt] for nt in reversed(seq))



def transcribe_dna(seq):
    pass


def has_start_codon(rna_seq):
    pass


import doctest
doctest.testmod()