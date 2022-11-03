#!/usr/bin/python

# Торговый автомат выдает сдачу монетами 1с, 10с, 25с, 50с, 1$,
# при внесенной сумме 5$ и цене товара 0.99$ должен вернуть сдачу наименьшим кол-ом монет,
# в виде списка кол-ва монет каждого имеющегося в автомате номинала,
# т.е. ответ должен быть [1, 0, 0, 0, 4] для примера выше
#
# assert(get_change(5, 0.99) equals([1, 0, 0, 0, 4])

# Реализовал лобовой алгоритм, но он даёт требуемый результат не для любых наборов номиналов
# чтобы уйти от float, доллары оставил только на get_change, а внутри все расчёты в центах
# потом подсмотрел в гугле и узнал, что задача знаменитая, лобовой алгоритм называется жадным а набор номиналов,
# для которого он даёт оптимальный результат - каноническим

coins_available = [1, 10, 25, 50, 100]

def get_max_under_ceil(ceil, array):
    for value in reversed(sorted(array)):
        if value <= ceil:
            return value
    return 0


def get_change(sum_paid, price, coins_available):
    change = [0] * len(coins_available)
    sum_paid_scaled = round(sum_paid * 100)
    price_scaled = round(price * 100)

    while sum_paid_scaled > price_scaled:
        decrement = get_max_under_ceil(sum_paid_scaled - price_scaled, coins_available)
        sum_paid_scaled = sum_paid_scaled - decrement
        change[coins_available.index(decrement)] += 1
    return change


if __name__ == '__main__':
    print(get_change(5, 0.99, coins_available))
