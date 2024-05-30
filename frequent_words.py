

def frequent_words(dna, k):
    all_k_mers = {}
    if len(dna) < k:
        return "Invalid"
    if len(dna) == k:
        return dna
    kmer = ""
    i = 0
    max = 0
    max_kmer = ""
    while(i < len(dna)):
        kmer = dna[i:i+k]
        if kmer in all_k_mers:
            all_k_mers[kmer] += 1
        else:
            all_k_mers[kmer] = 1
        i += 1
        if all_k_mers[kmer] > max:
            max_kmer = kmer
            max = all_k_mers[kmer]
    return max_kmer

max_kmer = frequent_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
print(max_kmer)




        