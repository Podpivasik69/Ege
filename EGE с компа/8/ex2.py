from itertools import *

a = sorted("ГЕРМАНИЯ")

n = 0

for x in product(a, repeat=6):
    n += 1
    x = ''.join(x)
    print(f'{n}: {x}')

    if n % 2 == 0:
        if x[0] != "Г" and x.count('И') == 2:
            if x.count("Л") >= 3:
                print(n, x)
                break
