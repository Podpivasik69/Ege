f = list(map(int, open('17_23276.txt').readlines()))
k = 0
m = -10 ** 100
n = 3

mf = max([x for x in f if str(x)[-2:] == '25'])

for i in range(len(f) + 1 - n):
    p = f[i: i + n]
    t = [len(str(abs(x))) == 4 for x in p]

    if t.count(True) <= 2 and sum(p) <= mf:
        print(p, t)
        m = max(m, sum(p))
        k += 1
print(k, m)
