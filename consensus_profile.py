# several homologous strands that we wish to analyze simultaneously, then the natural problem is to 
# find an average-case strand to represent the most likely common ancestor of the given strands.

def consensus_matrix(file_name):
    file = open(file_name)
    strings = [line.strip() for line in file]
    string = ""
    dna_strings =[]
    for dna in strings:
        if(dna[0] == '>'):
            if(string != ""):
                dna_strings.append(string)
                string = ""
        else:
            string += dna

    filtered_lst = dna_strings

    w, h = len(filtered_lst[0]), 4
    Matrix = [[0 for x in range(w)] for y in range(h)] 

    for i in range(0,len(filtered_lst)):
        for j in range(0,len(filtered_lst[0])):
            if(filtered_lst[i][j] == 'A'):
                Matrix[0][j] += 1
            elif(filtered_lst[i][j] == 'C'):
                Matrix[1][j] += 1
            elif(filtered_lst[i][j] == 'G'):
                Matrix[2][j] += 1
            else:
                Matrix[3][j] += 1
    print_consensus(Matrix)
    print_matrix(Matrix)

def print_matrix(Matrix):
    all_letter = ['A','C','G','T']
    for i in range(0,4):
        print("\n")
        print(all_letter[i] + ":", end= " ")
        for j in range(0,len(Matrix[i])):
            print(Matrix[i][j],end=" ")

def print_consensus(Matrix):
    all_letter = ['A','C','G','T']
    consensus = ""
    for i in range(0,len(Matrix[0])):
        highest_c = 0
        letter_i = 0
        for j in range(0,4):
            if(Matrix[j][i] > highest_c):
                letter_i = j
                highest_c = Matrix[j][i]
        consensus += all_letter[letter_i]
    print(consensus)
consensus_matrix("datasets/rosalind_cons.txt")
    