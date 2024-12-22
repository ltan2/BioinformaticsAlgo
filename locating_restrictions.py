def find_reverse_palindromes(dna, min_len=4, max_len=12):
    results = []
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for i in range(len(dna)):
        for length in range(min_len, max_len + 1):
            if i + length > len(dna):
                break
            substring = dna[i:i + length]
            reversed_str = ""
            for j in range(len(substring)):
                if complement[substring[j]] == substring[len(substring) - 1 - j]:
                    reversed_str = complement[substring[j]] + reversed_str
                else:
                    break
            if substring == reversed_str:
                results.append((i + 1, length))
    return results

palindromes = find_reverse_palindromes("TCAATGCATGCGGGTCTATATGCAT")

for position, length in palindromes:
    print(position, length)
