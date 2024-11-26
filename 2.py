def f(a):
    c = []
    count = 0
    for j in range(1, int(a ** 0.5) + 1):
        if a % j == 0:
            count += 1
    if float(a ** 0.5) != int(a ** 0.5):
        c.append(2 * count)
    else:
        c.append(2 * count - 1)

    return c


a = int(input())
print(*f(a))
