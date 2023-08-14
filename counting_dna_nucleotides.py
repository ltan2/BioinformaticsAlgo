# Biology background:
# Nucleus is filled with macromolecules
# One class is called nucleic acid
# Nucleic acid monomer == nucleotide
# Each nucleotide is formed of three parts: a sugar molecule, a negatively charged ion called a phosphate, and nucleobases
# DNA has for bases:  adenine (A), cytosine (C), guanine (G), and thymine (T).

def calculateFreqBases(DNA):
    freq_map = {'A': 0, 'C': 0, 'G':0, 'T': 0}
    for base in DNA:
        freq_map[base] += 1
    print(freq_map)

with open("rosalind_dna.txt","r") as f:
    dna = f.read().splitlines()

calculateFreqBases(dna[0])