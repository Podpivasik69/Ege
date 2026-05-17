# from sys import setrecursionlimit
#
# setrecursionlimit(10 ** 6)


def f(x, y, t=[1], p=''):
    if x > y:
        return 0
    if x == y:
        # print(t, p)
        return 1

    r = f(x + 1, y, t + [x + 1], p + '1')
    r += f(x * 2, y, t + [x * 2], p + '2')
    r += f(x + 2, y, t + [x + 2], p + '3')
    return r


a = f(7, 13)
b = f(13, 15)
c = f(15, 51)

d = f(15, 35)
e = f(35, 51)

print(a * b * (c - d * e))
# print(f(7, 51))
