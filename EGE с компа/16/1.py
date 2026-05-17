from sys import setrecursionlimit

setrecursionlimit(10 ** 6)


def f(n):
    if n < 10:
        return 3
    else:
        return (n + 4) * f(n - 5)

a = (f(257487) // 683 + 67 * f(257477)) // f(257472)

print(a)