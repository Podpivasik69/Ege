def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s


def f2(n):
    r = f(n)
    if n % 3 == 0:
        n += r[-2:]
    else:
        n += f(sum(map(int, r)) * 3)
    return int(r, 3)



m = 10**19
for _ in range(1, 1000):
    r = f2(_)
    d = abs(826 - r)
    if d < m:
        m = d
        mm = r

print(mm)