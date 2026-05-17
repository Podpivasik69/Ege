def p(x):
    if x <= 1:
        # число сложное
        return 0

    for d in range(2, int(x ** .5) + 1):
        if x % d == 0:
            return 0
    return 1


def dell(x):
    r = set()
    for d in range(2, int(x ** .5) + 1):
        if x % d == 0:
            if p(d) and '4' in str(d) or '7' in str(d):
                r.add(d)
            if p(x // d) and '4' in str(x // d) or '7' in str(x // d):
                r.add(x // d)
    r = list(r)
    if len(r) == 3 and r[0] * r[1] * r[2] == x:
        return min(r) + max(r)
    return 0


x = 2400000
k = 0

while k < 5:
    m = dell(x)
    if m > 0:
        print(x, m)
        k += 1
    x += 1
