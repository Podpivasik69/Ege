f = open('17_17530.txt').readlines()
f = list(map(int, f))
mf = min(f)
k = 0
n = 2
m = 10 ** 100

for i in range(len(f) - n + 1):
    p = f[i:i + n]

    t = [x % 55 == mf for x in p]

    if t.count(True) >= 1:
        k += 1
        m = min(m, sum(p))

print(k, m)
