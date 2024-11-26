from bisect import bisect

l = int(input())
a = list(map(int, input().split()))
if l == 1:
    print('1\n' + str(*a))
    exit(0)

d = [0 for _ in range(l)]
res = [[] for _ in range(l)]
for i in range(1, l):
    d[i] = a[i] - a[i - 1]


bisect()
neg_cnt = 0
for j in range (l):
    if d[j] <= 0:
        r = [a[j]]
        for i in range(j + 1, l):
            if d[i] < 0:
                neg_cnt += d[i]
                continue
            if d[i] + neg_cnt > 0:
                r.append(a[i])
        res[j] = r

res.sort(key = len)
mx = res[-1]

print(len(mx))
print(*mx)
