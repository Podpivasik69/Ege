# шаблон

# f = open('17_28762.txt').readlines()
# f = list(map(int, f))
#
# m = 10 ** 100
# n = 2
# k = 0
#
# for i in range(len(f) + 1 - n):
#     p = f[i:i + n]
#     k += 1
#     m = max(m, sum(p))
# print(k, m)

f = open('17_28762.txt').readlines()
f = list(map(int, f))

m = 10 ** 100
n = 2
k = 0

mf = min(x for x in f if abs(x) % 23 == 0)

for i in range(len(f) + 1 - n):
    p = f[i:i + n]
    t = [x % mf == 0 for x in p]
    if t.count(True) >= 1:
        k += 1
        m = max(m, sum(p))

print(k, m)
