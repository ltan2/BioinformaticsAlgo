# brute force: generate all possible supersequence and then get the shortest one
# so basically for each position, if match keep, else generate both ends if shift one vs shift next

#more efficient way is to make a queue for each base for each string
#then calculate when the next one will be

   
def initialize_map(stra, strb):
    mapa = {}
    mapb = {}

    # Build mapa
    for index, char in enumerate(stra):
        if char not in mapa:
            mapa[char] = []
        mapa[char].append(index)

    # Build mapb
    for index, char in enumerate(strb):
        if char not in mapb:
            mapb[char] = []
        mapb[char].append(index)

    return mapa, mapb

def main_function(stra, strb):
    map_a, map_b = initialize_map(stra, strb)
    final_string = ""

    i = 0
    j = 0

    while(i < len(stra) and j < len(strb)):
        if (stra[i] == strb[j]):
            final_string += stra[i]
            map_a[stra[i]].pop()
            map_b[strb[j]].pop()
            i += 1
            j += 1
        else:
            pos_a = 100
            pos_b = 100
            if strb[j] in map_a and len(map_a[strb[j]]) > 0:
                pos_a = map_a[strb[j]][0] # getting the position if I pick base_a
            if stra[i] in map_b and len(map_b[stra[i]]) > 0:
                pos_b = map_b[stra[i]][0] # getting the position if I pick base_b
            if pos_a > pos_b:
                #remove base_b current index from its map
                map_b[strb[j]].pop()
                final_string += strb[j]
                j += 1
            else:
                map_a[stra[i]].pop()
                final_string += stra[i]
                i += 1


    if i < len(stra):
        final_string += stra[i:len(stra)]
    elif j < len(strb):
        final_string += strb[j:len(strb)]
    else:
        final_string += ""

    return final_string

res = main_function("ATCTGAT","TGCATA")
print(res)
second_test = main_function("ACGTC","ATAT")
print(second_test)
