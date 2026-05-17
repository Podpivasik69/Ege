from itertools import *

a = sorted("СТРЕЛА")

n = 0

for x in product(a, repeat=5):
    n += 1
    x = ''.join(x)
    print(f'{n}: {x}')

    if n % 2 != 0:
        if x[0] != "А" and x[0] != "С" and x[0] != "Т" and x.count('Е') == 2:
            if x.count("Л") >= 3:
                print(n, x)
                break
