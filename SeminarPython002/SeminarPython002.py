# ЗАДАЧА: По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# ---------------------------------------------------------------------------------------------------------
# С циклом While:

# number = int(input('Введите целое число: '))
# i = 1
# fact = 1
# while i <= number:
#     fact *= i
#     i += 1
# print(f'Факториал числа {number} = {fact}')

# -----------------------------------------------------------------------------------------------------------
# С циклом for:

# number = int(input('Введите целое число: '))
# fact = 1
# for i in range(1, number + 1):
#     fact *= i
# print(f'Факториал числа {number} = {fact}')
# ================================================================================================================

# ЗАДАЧА: Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое
# # число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# number = int(input('Введите натуральное число больше 1: '))
# fib1 = 0
# fib2 = 1
# i = 0
# while i < number:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
#     if fib_sum == number:
#         print('Номер этого элемента:', i + 2)
#         break
# else:
#     print(-1)

# ====================================================================================================================
# ЗАДАЧА: Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза.Числа не превышают 30000
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# from random import randint
#
# count_watermelon = int(input('Введите количество арбузов: '))
#
# max_weight = 0
# min_weight = 30000
# for _ in range(1, count_watermelon + 1):
#     weight_watermelon = randint(1, 30000)
#     print(f'Вес арбуза {weight_watermelon}')
#     if max_weight < weight_watermelon:
#         max_weight = weight_watermelon
#     if min_weight > weight_watermelon:
#         min_weight = weight_watermelon
#
# print(f'Максимальный вес {max_weight}')
# print(f'Минимальный вес {min_weight}')
