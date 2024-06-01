# form a map of kmers
def frequent_words_mismatch(dna, k, d):
    all_k_mers = {}
    i =0
    while(i < len(dna)-k + 1):
        kmer = dna[i:i+k]
        if kmer in all_k_mers:
            all_k_mers[kmer] += 1
        else:
            all_k_mers[kmer] = 1
        i += 1

    max_kmers = {}
    for kmer1 in all_k_mers:
        all_match = []
        for kmer2 in all_k_mers:
            if kmer1 != kmer2:
                # check if its d + 1 mismatch
                i = 0 
                mismatches = 0
                while(i < len(kmer1)):
                    if kmer1[i] != kmer2[i]:
                        mismatches += 1
                    i += 1
                if mismatches <= d +1:
                    all_match.append(kmer2)
        print("kmer1: ", kmer1)
        print("kmer2: ", len(all_match))
                    

frequent_words_mismatch("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)

                    
        