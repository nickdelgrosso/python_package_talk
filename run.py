from genomics import get_dna_sequence, complement_dna, transcribe_dna, has_start_codon

seq = get_dna_sequence()

comp_seq = complement_dna(seq)

rna_seq = transcribe_dna(seq)
rna_comp_seq = transcribe_dna(comp_seq)

print(has_start_codon(rna_seq))
print(has_start_codon(rna_comp_seq))