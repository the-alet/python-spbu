n = int(input())
a = input()


def f(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10
    return s


b = list(map(int, a.split(' ')))
mxl = 0
for i in b: mxl = max(mxl, f(i))
c = n * [0]
m = (mxl + 1) * [0]
for i in range(n):
    m[mxl + 1 - f(b[i])] += 1
for i in range(1, mxl): m[i] += m[i - 1]
for i in range(n):
    q = f(b[i])
    w = m[mxl - q]
    c[w] = b[i]
    m[mxl - q] += 1
print(*c)
