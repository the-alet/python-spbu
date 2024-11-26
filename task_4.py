from random import *

def bfs(x, y, M, N):
    bw = []
    q = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    cq = [(x, y)]



    bw.sort(key=len)
    return bw[0]


#main
m, n = map(int, input().split())
mapa = [[0 for x in range(m + 2)] for y in range(n + 2)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        mapa[i][j] = 'x' if randint(1, 20) < abs((m / 2 - j) * (n / 2 - i)) + 7 else 'o'



mapb = [[-1 for x in range(m + 2)] for y in range(n + 2)]
mapa[n // 2][m // 2], mapb[n // 2][m // 2] = '*', 0

for i in range(1, n + 1):
    print(*mapa[i][1:m + 1])
for i in range(1, n + 1):
    print(*mapb[i][1:m + 1])
