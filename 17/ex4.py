f = list(map(int, open('17_27300.txt').readlines()))
k = 0
n = 3
m = 10**100

mf = max([x for x in f if abs(x) % 100 == 11])

for i in range(len(f) + 1 - n):
    p = f[i: i + n]

    t = [x < 0 for x in p]
    if t.count(True) == 0 and sum(p) >= mf:
        k += 1
        print(p, t)
        m = min(m, sum(p))

print(k, m)