f = open('17_27134.txt').readlines()
f = list(map(int, f))

mf = -10 ** 100
for i in range(len(f)):
    if len(str(abs(f[i]))) == 2 and abs(f[i]) % 10 == 3:
        if f[i] > mf:
            mf = f[i]

m = 10 ** 100
n = 2
k = 0

for i in range(len(f) - n + 1):
    p = f[i:i + n]
    t1 = [len(str(abs(x))) == 3 for x in p]
    # t2 = [int(str(x)[0]) % 2 == 0 for x in p]
    t2 = [str(abs(x))[0] in '2468' for x in p]
    if t1.count(True) == 1 and t2.count(True) == 2:
        if sum(p) % mf == 0:
            print(p, t1, t2)
            k += 1
            m = min(m, sum(p))
print(k, m)
