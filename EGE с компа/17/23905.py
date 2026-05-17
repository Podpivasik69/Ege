f = open('17_23905.txt').readlines()
f = list(map(int, f))
mf = max([x for x in f if str(x)[-2:] == '37'])
k = 0
n = 4
# m = -10 ** 100
s = 0
for i in range(len(f) - n + 1):
    p = f[i:i + n]

    t = [x for x in p if len(str(x)) > 1 and str(x)[-1] == str(x)[-2]]
    t2 = [x for x in p if x > mf]

    if len(t) == 1 and len(t2) == 2:
        k += 1
        # m = min(m, sum(p))
        s += sum([x for x in p if len(str(x)) >1 and str(x)[-1] == str(x)[-2]])
print(k, s)
