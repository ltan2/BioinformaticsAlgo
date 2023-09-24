def mortal_rabbits(n,m):
    big_small = [[0,0] for _ in range(n+1) ]
    big_small[0][1] = 1
    big_small[1][0] = 1
    for i in range(2,n):
        # update big      # prev_big + prev small
        big_small[i][0] = big_small[i-1][0] + big_small[i-1][1]
        # update small = prev big *  1
        big_small[i][1] = big_small[i-1][0] * 1
        if i >= m:
            # small from m months ago
            big_small[i][0] = big_small[i][0] - big_small[i-m][1] 
    print(big_small[n-1][0] + big_small[n-1][1])

mortal_rabbits(88,19)
  