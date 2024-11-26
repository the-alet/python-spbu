def find_min_max_values(E, F, N, coins):
    W = F - E
    inf = float('inf')
    
    min_value = [inf] * (W + 1)
    max_value = [-1] * (W + 1)
    
    min_value[0] = 0
    max_value[0] = 0
    
    for Pi, Wi in coins:
        for w in range(Wi, W + 1):
            if min_value[w - Wi] != inf:
                min_value[w] = min(min_value[w], min_value[w - Wi] + Pi)

    for Pi, Wi in coins:
        for w in range(Wi, W + 1):
            if max_value[w - Wi] != -1:
                max_value[w] = max(max_value[w], max_value[w - Wi] + Pi)

    if min_value[W] == inf:
        return "This is impossible."
    
    return min_value[W], max_value[W]

E, F = map(int, input().split())
N = int(input())
coins = [tuple(map(int, input().split())) for _ in range(N)]

result = find_min_max_values(E, F, N, coins)

if isinstance(result, str):
    print(result)
else:
    print(result[0], result[1])