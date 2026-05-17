# print('a b c d')
#
# for a in range(2):
#     for b in range(2):
#         for c in range(2):
#             for d in range(2):
#                 if (a <= b) and (b <= (not (c))) and (c == (not (d))) == 1:
#                     print(a, b, c, d)
#


print('a b c d')

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (a == b) or (not(c == d)) and (b <= (not (c))) == 0:
                    print(a, b, c, d)

