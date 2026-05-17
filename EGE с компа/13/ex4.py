from ipaddress import *

net = ip_network('136.36.240.16/29', 0)

full_pull = []
c = 0
for i in net:
    nice_i = bin(int(i))[2 + 21:]
    # print(nice_i)
    if nice_i.count('101') == 0:
        c += 1

print('-----------------')
print(c)
# for _ in full_pull:
#     print(_)
