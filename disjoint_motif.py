# whether two disjoint motifs can be located in a given string

def build_matrix(dna_str, list_of_str):
    cols = len(list_of_str)
    mat = [[0 for _ in range(cols)] for _ in range(cols)]
    for i in range(0,len(mat)):
        for j in range(i,len(mat)):
            if ret_str_cmp(dna_str, list_of_str[i], list_of_str[j]) == 1:
                print(dna_str + " " + list_of_str[i] + " " + str(i) + " " + str(j))
                mat[i][j] = 1
                mat[j][i] = 1
    return mat

def ret_str_cmp(dna_str, first_substr, sec_substr):

    for i in range(0,len(dna_str) - (len(first_substr) + len(sec_substr)) + 1):
        dna_substr = dna_str[i: i + len(first_substr) + len(sec_substr)]
        first_substr_p = 0
        sec_substr_p = 0
        dna_p = 0
        while(dna_p < len(dna_substr)):
            if first_substr_p < len(first_substr) and dna_substr[dna_p] == first_substr[first_substr_p]:
                dna_p += 1
                first_substr_p += 1
            elif sec_substr_p < len(sec_substr) and dna_substr[dna_p] == sec_substr[sec_substr_p]:
                dna_p += 1
                sec_substr_p += 1
            else:
                break
        if first_substr_p == len(first_substr) and sec_substr_p == len(sec_substr) and dna_p == len(dna_substr):
            return 1
        
    return 0
            




res = build_matrix("GACCACGGTT",["ACAG","GT","CCG"])
print(res)