def f(s):
    r = ''
    for i in range(10):
        if str(i) in s:
            r += str(i)
    if r == '':
        r = "NO"
    return r


a = input()
print(f(a))
