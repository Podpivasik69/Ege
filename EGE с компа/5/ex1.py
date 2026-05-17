def fork(n):
    origin = n
    n = bin(n)[2:]

    if origin % 3 == 0:
        n = n + n[-3:]
    else:
        ost = origin % 3
        ost -= 1
        ost *= 3
        n = n + bin(ost)[2:]

    return int(n, 2)


print(fork(12))
print(fork(5))

maxx = 0
for _ in range(1000000):
    if fork(_) < 416 and fork(_) > maxx:
        maxx = fork(_)

print(maxx)
# 411