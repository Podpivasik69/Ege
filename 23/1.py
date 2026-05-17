def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1

    r = f(x + 1, y)
    r += f(x * 2, y)
    return r


print(f(1, 10))