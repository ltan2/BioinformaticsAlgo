# brute force solution is to loop through each letter
# get the next k-1 words from it
# loop through text again and check how frequent words occur

# less brute force
# repeat step 1 and 2 above, but use hashmap to store result

def frequent_words(dna, k):
    all_k_mers = {}
    if len(dna) < k:
        return "Invalid"
    if len(dna) == k:
        return dna
    kmer = ""
    i = 0
    while(i < len(dna)):
        kmer = dna[i:i+k]
        if kmer in all_k_mers:
            all_k_mers[kmer] += 1
        else:
            all_k_mers[kmer] = 1
        i += 1
    return max(all_k_mers, key=all_k_mers.get)

max_kmer = frequent_words("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4)
print(max_kmer)




        