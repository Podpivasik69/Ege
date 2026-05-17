f = open("17_27629.txt").readlines()
f = list(map(int, f))

mf = max([x for x in f if len(str(abs(x))) == 4 and str(x)[-2:] == '43']) ** 2
k = 0
m = -10 ** 100

n = 2

for i in range(len(f) - n + 1):
    p = f[i:i + n]
    t = [len(str(abs(x))) == 4 for x in p]
    if t.count(True) >= 1 and (p[0] + p[1]) ** 2 < mf:
        # print(p, t)
        m = max(m, sum(p)**2)
        k += 1

print(k, m)
