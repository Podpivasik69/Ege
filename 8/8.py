from itertools import *

a = sorted("ОДСАЦЛФЩ")

n = 0

for x in product(a, repeat=4):
    n += 1
    x = ''.join(x)
    print(f'{n}: {x}')

    if n % 2 != 0:
        if x[0] != "А" and x[-1] != "А":
            if x.count("Л") >= 3:
                print(n, x)
                break
