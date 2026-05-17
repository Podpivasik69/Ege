f = list(map(int, open('17_23376.txt').readlines()))

k = 0
m = -10 ** 100
n = 2

mf = max([x for x in f if len(str(abs(x))) == 5 and abs(x) % 100 == 37]) ** 2

for i in range(len(f) + 1 - n):
    p = f[i: i + n]
    t = [len(str(abs(x))) == 5 for x in p]
    if t.count(True) == 1 and sum(p)** 2 > mf:
        k += 1
        print(p)
        m = max(m, sum(p))

print(k, m)
