from ipaddress import *

net = ip_network('192.168.32.160/28', 0)


c = 0
for i in net:
    nice_i = bin(int(i))[2:]
    print(nice_i)
    if nice_i.count('1') % 2 == 0:
        c += 1

print(c)