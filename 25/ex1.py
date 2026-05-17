def p(x):
    """ функция проверки являетяс ли чисто простым"""
    if x <= 1:
        return 0
    for d in range(2, int(x ** 0.5) + 1):
        if x % d == 0:
            return 0
    return 1  # простое


def fork(x):
    # r = list()  # список с повторами
    r = set()  # множество без повторов
    for d in range(2, int(x ** 0.5) + 1):
        #  твивиальные - 1 и само число
        # если ищем делители включая тривиальные (1, и x) то берем range(1
        # если тривиалтные не нужны то начинаем с 2, range(2
        if x % d == 0:
            # добавляем только простые чиса
            # если оно простое то добавляет
            if p(d):  # если оно простое
                # и число троек в нем 2 штуки
                r.add(d)
            if p(x // d):
                r.add(x // d)
    r = sorted(r)
    if r:
        return r
    return 0


k = 0
for _ in range(8996453, 10 ** 100):
    r = fork(_)
    if r and len(r) == 2 and r[0] * r[1] == _:
        k += 1
        print(_, max(r))
        if k == 5:
            break
