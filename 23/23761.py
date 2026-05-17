from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def f(x, y, t=[1], p=''):
    # global adasda
    if x < y:
        return 0
    if x == y:
        if 16 in t:
            print(t, p)
            return 1
        return 0

    r = f(x - 2, y, t + [x - 2], p + '1')
    r += f(x // 2, y, t + [x // 2], p + '2')
    return r


print(f(48, 2))
