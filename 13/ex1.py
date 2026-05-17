from heapq import nlargest
from ipaddress import *

n = ip_network('192.168.32.64/255.255.255.192', 0)
k = 0
# 255.255.255.192 = /26

for x in n:
    ip = bin(int(x))
    if bin(int(x))[-4:] == '1010':
        print(x, ip)
        k += 1
print(k)
