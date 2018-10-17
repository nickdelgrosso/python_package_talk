
seq = get_dna_sequence()

comp_seq = complement_dna(seq)

rna_seq = transcribe_dna(seq)
rna_comp_seq = transcribe_comp_dna(seq)

print(has_start_codon(rna_seq))
print(has_start_codon(rna_comp_seq))