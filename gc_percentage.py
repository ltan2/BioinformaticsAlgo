# Human genome are about 99% similar to one another
# cytosine and guanine will always have same percentage in dna
# in practice, eukaryotes have around 50%, prokaryotes have 50% or greater GC content
# FASTA Format of specifying dna strings:
# >Rosalind_6404
# CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCCCCACTAATAATTCTGAGG
# >Rosalind_5959
# CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC
# use > to denote this is the label

def highest_percentage():
    with open("datasets/rosalind_gc.txt","r") as f:
        label_and_dna = f.read().splitlines()
    labels = []
    dna_strings = []
    string_dna = ""
    for dna in label_and_dna:
        if dna[0] == '>':
            labels.append(dna[1:])
            if string_dna != "":
                dna_strings.append(string_dna)
                string_dna = ""
        else:
            string_dna += dna
    print(labels)
    print(len(dna_strings))
    highest_gc = 0
    index = 0 
    highest_gc_index = 0
    for dna_string in dna_strings:
        gc = 0
        for base in dna_string:
            if(base == 'G' or base == 'C'):
                gc += 1
        percent_gc = gc / len(dna_string)
        if percent_gc > highest_gc:
            highest_gc = percent_gc
            highest_gc_index = index
        index += 1

    print(labels[highest_gc_index])
    print(highest_gc)

highest_percentage()





