# A mutation is simply a mistake that occurs during the creation or copying of a nucleic acid, 
# in particular DNA.
# The simplest and most common type of nucleic acid mutation is a point mutation, which replaces one base with another at a single nucleotide
# In the case of DNA, a point mutation must change the complementary base accordingly
# Two DNA strands taken from different organism or species genomes are homologous if they share a recent ancestor

def hamming_dna(dna1, dna2):
    dist = 0
    for i in range(0,len(dna1)):
        if dna1[i] != dna2[i]:
            dist += 1
    print(dist)

with open("datasets/rosalind_hamm.txt","r") as f:
    dnas = f.read().splitlines()
hamming_dna(dnas[0],dnas[1])