def at_most_d(pattern, text, d):
    mismatch = 0
    for i in range(0,len(pattern)):
        if pattern[i] != text[i]:
            mismatch += 1
    if mismatch <= d:
        return True
    return False

def approximate_mismatch(pattern, text, d):
    i = 0
    ret_position = []
    while(i < len(text)-len(pattern)):
        acceptable_mismatch = at_most_d(pattern,text[i:i+len(pattern)],d)
        if acceptable_mismatch:
            ret_position.append(i)
        i+=1
    return ret_position

all_positions = approximate_mismatch("ATTCTGGA","CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC", 3)
print(all_positions)
