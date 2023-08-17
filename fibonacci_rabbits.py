# Counting rabbits the fibonacci way
# https://rosalind.info/problems/fib/

def fibonacci_rabbits(n, k):
    table = [0 for _ in range(n+1)]
    table[0] = 1
    table[1] = 1
    x = range(2,n)
    for i in x:
        table[i] = table[i-1] + table[i-2] * k
    print(table[n-1])

fibonacci_rabbits(32,5)

