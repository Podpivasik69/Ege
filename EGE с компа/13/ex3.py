from ipaddress import *

mask = bin(int(ip_address('255.255.248.0')))[2:]

print(2 ** mask.count('0') - 1046 - 2)
