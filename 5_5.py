import sys
from itertools import combinations

def hamming_dist(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def gen_hamming_dist_strs(k, s):
    n = len(s) # max length of the bit string
    all_strings = []

    # Generate all possible bit strings of length n
    for i in range(2**n):
        candidate = f"{{:0{n}b}}".format(i)  # Convert to binary with leading zeros
        if hamming_dist(candidate, s) == k:
            all_strings.append(candidate)

    return all_strings

k = int(input("Enter the Hamming distance: "))
s = input("Enter the bit string: ")
# Generate and print all bit strings with Hamming distance k
result = gen_hamming_dist_strs(k, s)
print(' '.join(result))
