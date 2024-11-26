from random import randint
import os
pr = 0
isPrinted = 0
n = 10**6
f = open('gen1.txt', 'w')
for i in range(n):
    f.write(str(randint(1,1000000)) + " ")
    if pr != (100 * i // n):
        pr = (100 * i // n)
        isPrinted = 0
    if isPrinted == 0 and pr % 10 == 0:
        print(str(pr) + '%')
        isPrinted = 1
f.close()
