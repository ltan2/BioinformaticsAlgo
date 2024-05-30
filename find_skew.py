def find_skew(genome):
    all_positions = [0 for i in range(0, len(genome)+1)]
    c = 0
    g = 0
    min_val = 0
    skewed_position = []
    for i in range(0,len(genome)):
        base = genome[i]
        all_positions[i] = abs(c-g)
        if base == 'C':
            c +=1
        elif base == 'G':
            g +=1
        if all_positions[i] > min_val:
            min_val = all_positions[i]

    for j in range(0,len(all_positions)):
        if all_positions[j] == min_val:
            skewed_position.append(j)
    print(skewed_position)

genome = "CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG"
find_skew(genome)