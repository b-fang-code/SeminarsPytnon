# ЗАДАЧА:Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# from random import randint
#
# list_1 = []
# result = 0
# for i in range(15):
#     list_1.append(randint(1, 15))
# print(list_1)
# set_list = set(list_1)
# for i in set_list:
#     if list_1.count(i) // 2 > 0:
#         result += list_1.count(i) // 2
#
# print(f'Всего пар {result}')

# ====================================================================================================================
# ЗАДАЧА: Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

k = int(input('Введите предел: '))


def sum_friend(number: int):
    summa = 0
    for num in range(1, number):
        if number % num == 0:
            summa += num
    return summa


for n in range(1, k):
    for m in range(1, k):
        if (sum_friend(n) == m) and (sum_friend(m) == n) and (n != m):
            print(n, m)

