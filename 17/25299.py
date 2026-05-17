f = open('17_25299.txt').readlines()
f = list(map(int, f))

mf = max([x for x in f if len(str(x)) == 2])

k = 0
n = 3
m = 10 ** 100

for i in range(len(f) - n + 1):
    p = f[i:i + n]
    t = [x > 0 for x in p]
    if t.count(True) == 2 and sum(p) % mf == 0:
        print(p, t)
        k += 1
        m = min(m, sum(p))

print(k, m)
