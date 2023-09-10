# motif: commonly shared DNA interval
# repeats occur far more often than would be dictated by random chance,
# indicating that genomes are anything but random 
# The most common repeat in humans is the Alu repeat, which is approximately 300 bp long 
# and recurs around a million times throughout every human genome 
# Alu is parasitic: when a new Alu repeat is inserted into a genome, it frequently causes genetic disorders.

# using KMP algorithm because time complexity is only O(stra + strb) instead of the naive search that has
# time complexity of O(stra * strb)
# def motif_calc(stra, strb):

def kmp_algo(stra,strb):
    print(len(stra))
    all_indexes = []
    lps_table = kmp_table(strb)
    i = 0
    j = 0
    while(i < len(stra)):
        if(stra[i] == strb[j]):
            i += 1
            j += 1
        else:
            if(j == 0):
                i += 1
            else:
                j = lps_table[j-1]
        if(j == len(strb)):
            all_indexes.append(i-j+1)
            j = lps_table[j-1]
    for index in all_indexes:
        print(index,end=" ")

def kmp_table(strb):
    lps_table = [0] * len(strb)
    i = 1
    j = 0
    while(i < len(strb)):
        if(strb[i] == strb[j]):
            lps_table[i] = j + 1
            j +=1
            i += 1
        elif(j == 0):
            lps_table[i] = 0
            i += 1
        else:
            j = lps_table[j-1]
    return lps_table

kmp_algo("AAGCTCTAGCAAGCTCTACCGAGCTCTAAGCTCTAAGCTCTAATAAGAGCTCTACAGTGAGCTCTACAAGCTCTATAGCTCTATCCCAGCTCTAAAGCTCTAGAATTCAGCTCTAGCTAGCTCTATATATGAGCTCTAAGCTCTAAGCTCTACAGCTCTATAGCTCTAAATAAGCTCTATCTAGCTCTAAGCTCTACTTTAGCTCTATAAGCTCTACTTGCAAGCTCTACGGATATGAGCTCTAGCGAGCTCTAGGGACAAAGCGCAACGAGCTCTACAGCTCTAAGCTCTACAGCTCTATTAAGCTCTACCAGCTCTAATGGAGCTCTAGTGGTTAAAGCTCTATGAGCTCTACAAGCTCTACGGAGCTCTAGGAGCTCTAATGTGGATATTCAGCTCTAAGCTCTAACATAGCTCTACTGAGCTCTAAGCTCTAGAGCTCTAAGCTCTAAGCTCTAAGCTCTAGTATCATAGAAGCTCTAAGCTCTACACCAGCTCTAAGCTCTATAGCTCTAAGCTCTAAGCTCTACAAGCTCTACGAGCTCTACTATAGCCGAGCTCTAAGAGAGCTCTACAGCTCTAAGCTCTACATAGCTCTAAGCTCTATAGCTCTAAGCTCTACATATAACTAGCTCTATAGCTCTAAGCTCTACTCTAAGCTCTATTGCTAGCTCTAAGAGCTCTACCGAGTGCTAGCTCTAGTAGCTCTATCAGCTCTATAGCTCTAATAGCTCTAAGCTCTAGAAAGCTCTAACAGCTCTATCGTAGCTCTACAAAGCTCTAAAAGCTCTAGTCAACTACGGTACAGCTCTAATGCCACCAGCTCTAACAGCTCTAAGCTCTAAGCTCTACAGCTCTAACAGCTCTAGATAATAAGCTCTA","AGCTCTAAG")
