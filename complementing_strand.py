# Watson and Crick proposed the following structure for DNA:
# The DNA molecule is made up of two strands, running in opposite directions.
# Each base bonds to a base in the opposite strand. 
# A-T and C-G
# the two strands twist together to form a double helix
# a complimentary to a base is a big pair

def reverse_complement(strand):
    reverse_strand = ""
    for base in strand:
        if base == 'A':
            reverse_strand = 'T' + reverse_strand 
        elif base == 'T':
            reverse_strand = 'A' + reverse_strand
        elif base == 'G':
            reverse_strand = 'C' + reverse_strand
        else:
            reverse_strand = 'G' + reverse_strand
    print(reverse_strand)

with open("datasets/rosalind_revc.txt","r") as f:
    dna = f.read().splitlines()

reverse_complement(dna[0])