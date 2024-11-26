from random import *
import time
from termcolor import colored
import os

m, n = map(int, input().split())
t0 = time.time()
os.system('color')
mx = 6
cnt = [(0, []) for _ in range(mx)]
mapa = [[0 for x in range(m + 2)] for y in range(n + 2)]
lq = []

    
for i in range(1, n + 1):
    for j in range(1, m + 1):
        mapa[i][j] = randint(1, mx)
#for i in range(1, n + 1):
#    print(*mapa[i][1:m + 1])
        
def bfs(x, y):
    c = 1
    w = [[0 for x in range(m + 2)] for y in range(n + 2)]
    q = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    cq = [(x, y)]

    w[y][x] = 1

    while len(q) > 0:
        a = q[0]
        if w[a[1]][a[0]]:
            q = q[1:]
            continue

        w[a[1]][a[0]] = 1
        if mapa[a[1]][a[0]] == mapa[y][x]:
            d1, d2, d3, d4 = (a[0] + 1, a[1]), (a[0] - 1, a[1]), (a[0], a[1] + 1), (a[0], a[1] - 1)

            if d1 not in q: q.append(d1)
            if d2 not in q: q.append(d2)
            if d3 not in q: q.append(d3)
            if d4 not in q: q.append(d4)
            c += 1
            cq.append(a)

        q = q[1:]
    #print("bfs", x, y)    
    return c, cq
    
        
for i in range(1, n + 1):
    for j in range(1, m + 1):
        cnt[mapa[i][j] - 1] = max(cnt[mapa[i][j] - 1], bfs(j, i), key = lambda l: l[0])
        #print(j - 1, i - 1)

cols: list = ['red', 'green', 'cyan', 'yellow', 'magenta', 'blue']

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(mapa[i][j] if (j, i) not in cnt[mapa[i][j] - 1][1] else colored(str(mapa[i][j]), cols[mapa[i][j] - 1]), end=' ')
    print('')

mmx = max(cnt, key = lambda l: l[0])
mmxi = cnt.index(mmx)
print(mmx[0], '\''+ colored(str(mmxi + 1), cols[mmxi])+ '\'')
t1 = time.time()
print("worktime: ", t1 - t0)