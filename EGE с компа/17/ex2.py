f = list(map(int, open('17_23563.txt').readlines()))
k = 0
m = -10 ** 100
n = 2

mf = min([x for x in f if x > 0 and abs(x) % 35 == 0])

for i in range(len(f) + 1 - n):
    p = f[i:i + n]

    if p[0] != p[1] and abs(p[0] - p[1]) % mf == 0:
        k += 1
        print(p)

        m = max(m, sum(p))

print(k, m)
