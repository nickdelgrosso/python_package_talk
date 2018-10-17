
complement_nts = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'T'}
complement_rna_nts = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

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

    Returns:
        comp_seq (str)

    Examples:
        >>> complement_dna('GGC')
        'GCC'

        >>> complement_dna('TTTGGC')
        'GCCAAA'
    """
    return ''.join(complement_nts[nt] for nt in reversed(seq))



def transcribe_dna(seq):
    """
    Transcribes DNA sequence to RNA sequence.

    Args:
        seq (str): a DNA sequence

    Returns:
        rna_seq (str): an RNA sequence

    Examples:
        >>> transcribe_dna('GTCAA')
        'UUGAC'
    """
    return ''.join(complement_rna_nts[nt] for nt in reversed(seq))


def has_start_codon(rna_seq):
    """
    Returns True if 'AUG' in the RNA sequence
    Args:
        rna_seq (str): an RNA sequence

    Returns:
        has_AUG (bool): whether AUG is in the RNA

    """
    return 'AUG' in rna_seq


import doctest
doctest.testmod()