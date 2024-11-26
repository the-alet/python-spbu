def f(a, b):
    c = a // b
    c *= b
    return a - c


b = int(input())
a = int(input())

print(f(a, b))
