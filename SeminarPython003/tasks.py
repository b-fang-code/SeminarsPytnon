# ЗАДАЧА: Дан список чисел. Определите сколько в нём встречается различных чисел

# import random
#
# my_list = []
# for _ in range(15):
#     my_list.append(random.randint(0, 9))
#
# print(my_list)
#
# print(set(my_list))

# =====================================================================================================================
# ЗАДАЧА: Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
#
# import random
#
# number = int(input('Введите длинну последовательности: '))
# k = int(input('На сколько нужно сместить последовательность?: '))
# my_list = []
# for _ in range(number):
#     my_list.append(random.randint(0, 9))
# print(my_list)
# i = 0
# while i < k:
#     my_list.insert(0, my_list[len(my_list) - 1])
#     my_list.pop(len(my_list) - 1)
#     i += 1
# print(my_list)

# -------------------------------------------------------------------------------------------------------------------

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#
# number = int(input('На сколько нужно сдвинуть список?: '))
#
# for i in range(number):
#     temp = list.pop(len(list) - 1)
#     list.insert(0, temp)
# print(list)

# -----------------------------------------------------------------------------------------------------------------
# Решение из методички:

# list_1 = [5, 4, 6, 7, 8, -10]
# k = int(input('Введите: '))
# k = k % len(list_1)
# list_result = list()
# for i in range(k):
#     list_result.append(list_1[len(list_1) - 1 - i])
# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
# print(list_result)

# ------------------------------------------------------------------------------------------------------------------
# Решение Стоуна:

# my_list = []
# for i in range(15):
#     my_list.append(i)
# print(my_list)
#
# shift = int(input('На сколько будем сдвигать? '))
# shift %= len(my_list)
#
# newest_list = my_list[-shift:]
# newest_list.extend(my_list[:-shift])
# print(newest_list)

# ==================================================================================================================
# ЗАДАЧА: Напишите программу для печати всех уникальных значений в словаре.

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"},
          {"VIII": "S007"}]

my_set = set()

for item in list_1:
    for key in item:
        my_set.add(item[key])

print(list_1)
print(my_set)

