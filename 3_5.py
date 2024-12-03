import sys
from itertools import combinations

def gen_combs(n):
    elements = [chr(i) for i in range(97, 97 + n)]  # Generate first n lowercase letters
    all_combinations = [""]

    # Generate combinations of all possible sizes
    for r in range(n + 1):
        for combo in combinations(elements, r):
            res = '\'' + ''.join(combo) + '\''
            all_combinations.append(res)

    return all_combinations

n = int(input("input a num from 1 to 26: "))
# Generate and print all combinations
result = gen_combs(n)
print(*result)
