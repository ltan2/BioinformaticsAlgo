#  Another defense mechanism found in the genomes of most bacteria and archaea centers on intervals of DNA called 
# CRISPRs (Clustered Regularly Interspaced Short Palindromic Repeats)
# which allow the cell to distinguish its own DNA from that of phages or plasmids.
# Specifically, a CRISPR is an interval of DNA consisting of identical repeats (approximately 23 to 47 bp long),
# alternating with unique intervals (approximately 21 to 72 bp long) called spacers
# Spacers correspond to fragments of foreign DNA that were integrated into the genome between repeats and serve 
# as a memory bank for genetic material captured from invading phages. 
# As a result, spacers can be used to recognize and silence invasive elements.
# Specifically, CRISPRs are transcribed into RNA molecules, each consisting of a spacer flanked by partial repeats. 
# The small CRISPR RNAs, together with associated proteins translated from this RNA, target foreign DNA that matches the CRISPR spacer. 
# In eukaryotes, a similar process is achieved by a process called RNA interference (RNAi).

# To locate a CRISPR in a genome, we need to search for its repeats. 
# We are looking for repeated intervals that cannot be lengthened in either direction (otherwise, we would intersect with a spacer).

def find_repeats(dna_str):
    unique_substr = {}
    for i in range (0,len(dna_str)):
        curr_longest = ""
        l_start = 0
        l_end = 0
        for j in range(20, len(dna_str)):
            substring = dna_str[i:i + j]
            if i + j > len(dna_str):
                break
            if substring in unique_substr:
                for each_p in unique_substr[substring]:
                    curr_pstart = each_p[0]
                    curr_pend = each_p[1]
                    if (get_prev(dna_str, curr_pstart) != get_prev(dna_str, i)) and (get_next(dna_str, curr_pend) != get_next(dna_str, i + j)):
                        if j > l_end - l_start:
                            curr_longest = substring
                            l_start = i
                            l_end = j
            else:
                unique_substr[substring] = [[i, i+j]]
        if curr_longest in unique_substr:
            unique_substr[curr_longest].append([l_start, l_end])
    
    for potential_rep in unique_substr:
        if len(unique_substr[potential_rep]) > 1:
            print(potential_rep)

def get_prev(dna_str, curr_i):
    if curr_i <= 0:
        return 'Z'
    else:
        return dna_str[curr_i - 1]

def get_next(dna_str, curr_i):
    if curr_i >= len(dna_str) - 1:
        return 'Z'
    else:
        return dna_str[curr_i + 1]
    

find_repeats("TAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTATTATATAGAGATAGAATGGGTCCAGAGTTTTGTAATTTCCATGGGTCCAGAGTTTTGTAATTTAT")