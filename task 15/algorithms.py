# -------------------------------------------------------------------------------------------------------------------- #
# ДЕЛИТЕЛИ:
for A in range(1, 10 ** 4):
    flag = True
    for x in range(1, 1000):
        if not ((x % A == 0) <= (x % 21 != 0 or x % 35 == 0)):
            flag = False
            break
    if flag:
        print(A)
        break
# -------------------------------------------------------------------------------------------------------------------- #
# ОТРЕЗКИ:


def F(X, T):
    return T[0] <= X <= T[1]


P, Q, R = (5, 100), (15, 25), (35, 50)
minA = 1000
for Ab in range(1, 150):
    for Ae in range(Ab + 1, 150):
        flag = True
        A = (Ab, Ae)
        for x in range(1, 150):
            if not (F(x, P) <= F(x, Q) or ((not F(x, A)) <= F(x, R))):
                flag = False
                break
        if flag and Ae - Ab < minA:
            minA = Ae - Ab
            break
print(minA)
# -------------------------------------------------------------------------------------------------------------------- #
