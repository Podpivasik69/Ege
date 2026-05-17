from ipaddress import *

net1 = ip_network(f'123.222.0.192/255.255.255.224', strict=True)
k = 0
for x in net1.hosts():
    n = bin(int(x))[2:].rjust(32, "0")
    if n.count("1") == n.count("0"):
        k += 1
print(k)
# 10
