#AACCTTGG
#ACACTGTGA
#res = AACTGG

# dynamic problem solution
def shared_spliced_motif(s1,s2):
    motif_matrix = [["" for i in range(0,len(s2)+ 1)] for j in range(0,len(s1) + 1)]

    # fill up matrix
    for i in range(len(s1) -1, -1, -1):
        for j in range(len(s2) -1, -1, -1):
            # both characters are equal in this case, check diagonal subproblem
            # e.g: AAA and AAC, A and A are equal, next case is AA is equal to AC?
            # we append curr char to common subsequence
            if s1[i] == s2[j]:
                motif_matrix[i][j] = s1[i] + motif_matrix[i+1][j+1]
            # longest subsequnce might be between AAA and AC or AA and AAC
            else:
                if len(motif_matrix[i+1][j]) > len(motif_matrix[i][j+1]):
                    motif_matrix[i][j] = motif_matrix[i+1][j]
                else:
                    motif_matrix[i][j] = motif_matrix[i][j+1]

    return motif_matrix[0][0]

lcs = shared_spliced_motif("AACCTTGG", "ACACTGTGA")
print(lcs)

