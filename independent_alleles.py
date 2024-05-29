# Mendel's first law states that for any factor, an individual randomly assigns one of its two alleles
# Mendel's second law states that  that alleles for different factors are inherited with no dependence on each other. 
# Aa = 0.5
# Bb = 0.5
# AaBb = 0.25
# Binomial distribution cumulative formula:
import math 

def ind_alleles(k,n):
    probability = 0
    for i in range(k, n + 1): 
        prob = (math.factorial(n) /
                (math.factorial(i) * math.factorial(n - i))) * (0.25 ** i) * (0.75 ** (n - i))
        probability += prob
    print(probability)

ind_alleles(37, 2 ** 7)