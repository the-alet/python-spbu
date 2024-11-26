a = float(input())
n = int(input())
ans = 0
c = 9
diff = ans ** n - a
while diff> 10 ** -11 or diff < -1 * (10 ** -11):
    temp = ans + 2 ** c
    if temp ** n <= a:
        ans = temp
    c -= 1
    diff = ans ** n - a
print(ans)
