def read_file(file_name):
    file = open(file_name)
    strings = [line.strip() for line in file]
    
    dna_strings =[]
    for dna in strings:
        if(dna[0] != '>'):
            dna_strings.append(dna)
    return dna_strings

def create_matrix(dna_strings):
    matrix = [[0 for i in range(len(dna_strings))] for j in range(len(dna_strings))]
    # first str sees the rest, second see third rest, etc
    for i in range(len(dna_strings)):
        for j in range(i+1,len(dna_strings)):
            ## fill diagonal
            matrix[i][j] = count_val(dna_strings[i], dna_strings[j])
            matrix[j][i] = matrix[i][j]
    print(matrix)

def count_val(s1, s2):
    diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff += 1
    return diff/len(s1)

dna_strings = read_file("datasets/rosalind_distmatrix.txt")
create_matrix(dna_strings)



