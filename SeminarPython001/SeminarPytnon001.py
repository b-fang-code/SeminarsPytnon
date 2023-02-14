# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении нельзя пользоваться условной инструкцие if и циклами


# a = int(input('Нужно проехать за день: '))
# b = int(input('Нужно проехать километров: '))
# c = round(b/a, 3)
# print(f'Потребуется {c} дней')

# ---------------------------------------------------------------------------------------------------------------
# Решение с библиотекой Math:
#
# import math
#
# n = 700
# m = 750
# print(math.ceil(m/n))


# ------------------------------------------------------------------------------------------------------------
# Решение Стоуна:

# dist_per_day = int(input('Машина за день проезжает: '))
# total_dist = int(input('Сколько проедет наша машина:'))
# days = ((total_dist + dist_per_day - 1) // dist_per_day)
# print(days)


# ====================================================================================================================
# ЗАДАЧА: Дано натуральное число. Требуется определить, является ли год с данным номером високосным.Если год является
# високосным, то выведете YES, иначе выведите No. Напомним, что в соответствии с григорианским кадендарем, год является
# високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.

# year = int(input('Введите год: '))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# ====================================================================================================================
# ЗАДАЧА! Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа
# - 6,78 -> 7
# - 5 -> нет
# - 0,34 -> 3


number = float(input('Введите число:'))
if number == int(number):
    print('Нет')
else:
    print(int(number * 10 % 10))