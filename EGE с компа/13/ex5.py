from ipaddress import *

net = ip_network('212.192.32.96/27', 0)

c = 0

for i in net:
    nice_i = bin(int(i))[2 + 24::]
    print(nice_i)
    if '111' not in nice_i and '000' not in nice_i:
        c += 1

print(c)
