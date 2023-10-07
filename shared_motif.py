# The simplest such region of similarity is a motif occurring without 
# mutation in every one of a collection of genetic strings taken from a 
# database; such a motif corresponds to a substring shared by all the strings. 
# We want to search for long shared substrings, as a longer motif will likely indicate a greater shared function.
from fasta_processor import get_sequence_label

def shared_motif(dna_strings):
    lgnst_substr = dna_strings[0]

    for i in range(1,len(dna_strings)):
        lgnst_substr = find_substr(dna_strings[i],lgnst_substr)
    print(lgnst_substr)

def find_substr(str1,str2):
    m = len(str1)
    n = len(str2)
    dp_str = [[0 for i in range(n + 1)] for j in range(m +1)]
    len_substr = 0
    row, col = 0,0
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp_str[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp_str[i][j] = dp_str[i - 1][j - 1] + 1
                if len_substr < dp_str[i][j]:
                    len_substr = dp_str[i][j]
                    row = i
                    col = j
            else:
                dp_str[i][j] = 0
    if len_substr == 0:
        return ""
    resultStr = ['0'] * len_substr
 
    # traverse diagonally
    while dp_str[row][col] != 0:
        len_substr -= 1 # or Y[col
        resultStr[len_substr] = str1[row - 1]
 
        # move diagonally up to previous cell
        row -= 1
        col -= 1
 
    # required longest common substring
    substr = ''.join(resultStr)

    return substr

shared_motif(get_sequence_label("datasets/rosalind_lcsm.txt")[0])