# e.g:
#5
#5 1 4 2 3
#Sample Output
#1 2 3
#5 4 2


def longest_increasing_subsequence(sequence, prev, res):
    # 5,1,4,2,3
    if len(sequence) == 0:
        return res
    
    res1 = []
    res2 = []
    
    curr = sequence[0]
    res_seq = sequence[1:]

    if curr > prev:
        res_with_curr = res[:]  # Copy of res
        res_with_curr.append(curr)
        res1 = longest_increasing_subsequence(res_seq, curr, res_with_curr)
    res2 = longest_increasing_subsequence(res_seq, prev, res) 


    if len(res1) > len(res2):
        return res1
    return res2   
        

res = longest_increasing_subsequence([5,1,4,2,3], -1, [])
print(res)