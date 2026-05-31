# def dvo(x):
#     s = ''
#     while x > 0:
#         s = str(x % 2) + s
#         x //= 2
#
#     return s
#
#
# def fork(x):
#     template = x
#     x = dvo(x)
#     a = str(x)
#     c = 0
#     for _ in range(2):
#         c = a.count('1')
#         # print(c)
#         # print(str(c % 2))
#         a = a + str(c % 2)
#     return int(a, 2)
#
#
# # print(dvo(25))
# # fork(7)
#
# for x in range(1, 10000):
#     f = fork(x)
#     if f > 253:
#         print(x)
#         break


# def tro(_1):
#     s = ''
#     while _1 > 0:
#         s = str(_1 % 3) + s
#         _1 //= 3
#     return s
#
#
# def fork(n):
#     s = tro(n)
#     if n % 3 == 0:
#         s = '1' + s + '02'
#     elif n % 3 != 0:
#         ost = n % 3
#         s = s + tro(ost * 4)
#     return s
#
#
# s = fork(12)
# print(s)
# print(int(s, 3))
# print('-----------')
#
#
# maxx = 0
# for n in range(1, 201):
#     x = fork(n)
#     r = int(x, 3)
#     if r < 199:
#         maxx = n
#
# print(maxx)


# def octo(_1):
#     s = ''
#     while _1 > 0:
#         s = str(_1 % 8) + s
#         _1 //= 8
#     return s
#
# # print(octo(230))
#
#
# def fork(n):
#     a = octo(n)
#
#     if int(a) % 2 == 0:
#         a += a[-1]
#         # print(a)
#     else:
#         first = a[0]
#         last = a[-1]
#         a = last + a[1:-1] + first
#         # print(a)
#     return a
#
#
#
# print(octo(123))
# print('////////')
# fork(123)
# maxx  = 0
# for n in range(1, 255):
#     r = fork(n)
#
#
#     if int(r, 8) < 254:
#         print(n, int(r, 8))


def dva(x):
    s = ''
    while x > 0:
        s = str(x % 2) + s
        x //= 2
    return s

print(dva(45))
def fork(x):
    y = dva(x)
    if x % 2 == 0:
        null_x = y.count('0')
        y += null_x * '0'
    else:
        ed_x = y.count("1")
        y = ed_x * '1' + y
    return y

maxx = 0
for n in range(1, 1000):
    r = fork(n)
    print(n, r, int(str(r), 2),)
    if int(r, 2) > 2000:
        print(f'N = {n}, R = {int(r, 2)}')
        



print(fork(47))
print(int(str(fork(49)), 2))
