# k =kmer length
# t = frequency at which k occurs in genome
def find_clump_genome(k,genome, t):
    #get all kmers
    all_clumps_t_times = []
    i = 0
    all_k_mers = {}
    while(i < len(genome)):
        kmer = genome[i:i+k]
        if kmer in all_k_mers:
            all_k_mers[kmer] += 1
        else:
            all_k_mers[kmer] = 1
        i += 1
        if all_k_mers[kmer] == t:
            if kmer not in all_clumps_t_times:
                all_clumps_t_times.append(kmer)
    return all_clumps_t_times

ret_clump = find_clump_genome(5,"CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC",4)
print(ret_clump)
