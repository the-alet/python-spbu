def f(arr):
    from bisect import bisect_left

    if not arr:
        return []

    lis = []
    prev_index = [-1] * len(arr)
    lis_indices = []

    for i in range(len(arr)):
        pos = bisect_left(lis, arr[i])
        if pos == len(lis):
            lis.append(arr[i])
            lis_indices.append(i)
        else:
            lis[pos] = arr[i]
            lis_indices[pos] = i
        
        if pos > 0:
            prev_index[i] = lis_indices[pos - 1]

    result = []
    k = lis_indices[-1]
    while k != -1:
        result.append(arr[k])
        k = prev_index[k]

    result.reverse()
    return result

N = int(input())
arr = list(map(int, input().split()))

lis = f(arr)

print(len(lis))
print(" ".join(map(str, lis)))
            
