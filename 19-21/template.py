def f(a, b, c, m):
    if a + b >= 65:
        return c % 2 == m % 2
    if c == m:
        return 0
    h = [f(a + 1, b, c + 1, m),
         f(a * 3, b, c + 1, m),
         f(a, b + 1, c + 1, m),
         f(a, b, c + 1, m)]
    if (c + 1) % 2 == m % 2:
        return any(h)
    else:
        return all(h)


b = 6
for a in range(1, 59):
    for m in range(1, 5):
        if f(a, b, 0, m):
            if m == 2:
                print(a)
            break
