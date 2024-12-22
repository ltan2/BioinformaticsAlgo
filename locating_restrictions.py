def reverse_complement(seq):
    reverse_seq = ""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in seq:
        reverse_seq += complement[base]
    return reverse_seq

def find_reverse_palindromes(dna, min_len=4, max_len=12):
    results = []
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in seq:
    for i in range(len(dna)):
        for length in range(min_len, max_len + 1):
            if i + length > len(dna):
                break
            substring = dna[i:i + length]
            for base in seq:
        reverse_seq += complement[base]
            if substring == reverse_complement(substring):
                results.append((i + 1, length))
    return results

palindromes = find_reverse_palindromes("TCAATGCATGCGGGTCTATATGCAT")

for position, length in palindromes:
    print(position, length)
