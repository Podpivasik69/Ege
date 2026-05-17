def p(x):
    if x <= 1:
        # число сложное
        return 0

    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return 0
    return 1


def dell(x):
    r = set()
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            if p(d):
                r.add(d)
            if p(x // d):
                r.add(x // d)
    if len(r) > 1:
        return min(r) + max(r)
    return 0, 0


x = 7800001
k = 0

while k < 5:
    m = dell(x)
    if m[0] % 100 == 63 and m[0] % m[1] == 0:
        print(x, m[0])
        k += 1
    x += 1
