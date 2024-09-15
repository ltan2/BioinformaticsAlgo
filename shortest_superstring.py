def shortest_superstring(str_arr):
    res_str = ""
    for strs in str_arr:
        right = add_to_string(res_str, strs)
        # add to res all str from right
        res_str += strs[right:]
    return res_str

def add_to_string(str1, str2):
    left = 0
    right = 0

    while(left < len(str1) and right < len(str2)):
        if str2[right] == str1[left]:
            right += 1
        else:
            right = 0
        left += 1
    
    return right

res = shortest_superstring(["ATTAGACCTG", "CCTGCCGGAA", "AGACCTGCCG", "GCCGGAATAC"])
if "ATTAGACCTGCCGGAATAC" == res:
    print("Passed implementation")

