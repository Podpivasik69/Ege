from ipaddress import *

net = ip_network('123.222.111.192/255.255.255.248', 0)

print(net)
c = 0
for i in net:
    nice_i = bin(int(i))[2 + 24:]
    if (nice_i.count('1') % 3) != 0:
        c += 1
    print(nice_i)

print(c)