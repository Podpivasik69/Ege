print("x y z w")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (not(a and not(c))   and not((c <= d)  and   (d <= c)) and b) == 1:
                    print(a, b, c, d)
