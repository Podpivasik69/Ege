f = open('26_28945.txt').readlines()
n = int(f.pop(0))
f = [list(map(int, x.split())) for x in f]

# print(f)
a = []
for x in f:
    a += [x[0], x[0] + x[1]]

a = sorted(a, key=lambda x: (x[1]))
print(a)

while a:
    t = a[0]
    a = [x for t in a if x[0] > t[1]]
