from fasta_processor import get_sequence_label

def overlap_graphs(dna_str,label):
    first_3_map = {}
    for i in range(0,len(dna_str)):
        first_3 = dna_str[i][0] + dna_str[i][1] + dna_str[i][2]
        if(first_3_map.get(first_3)):
            first_3_map[first_3].append(label[i])
        else:
            first_3_map[first_3] = [label[i]]
    last_3_map = {}
    for i in range(0,len(dna_str)):
        last_3 = dna_str[i][-3:]
        if(first_3_map.get(last_3)):
            j = 0
            for all_l in first_3_map[last_3]:
                if(label[i] != all_l):
                    print(label[i] + " " + all_l)
                j += 1

dna_str,label = get_sequence_label("datasets/rosalind_grph.txt")
overlap_graphs(dna_str,label)



         