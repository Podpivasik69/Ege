from itertools import *

a = sorted('ГЕРМАНИЯ')

k = 0
n = 0

for x in product(a, repeat=6):
    n += 1
    x = ''.join(x)


    if n % 2 == 0 and x[0] != 'Г' and x.count("И") >= 2:
        print(f'{n}: {x}')
        k += 1

print(k)
# 25165