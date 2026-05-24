def tro(x):
    s = ''
    while x > 0:
        s = str(x % 3) + s
        x = x // 3
    # print(s)
    return s


def fork(x):
    r = tro(x)

    chet = len([y for y in str(r) if int(y) % 2 == 0])
    nechet = len([y for y in str(r) if int(y) % 2 != 0])
    # print(x, chet, nechet)

    if chet > nechet:
        r += r[-2:]

    else:
        rr = ''
        for y in r:
            if y == '0':
                rr += '1'

            if y == '1':
                rr += '2'

            if y == '2':
                rr += '0'

            r = rr

    return int(r, 3)


print(fork(15))

m = 0
for x in range(1, 10000):
    r = fork(x)
    if r < 315:
        m = max(m, r)

print(m)
