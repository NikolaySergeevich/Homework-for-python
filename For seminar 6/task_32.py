# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)


# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
from random import randint


def Creat_lst():
    size = randint(14, 20)
    lst = [randint(-15, 15) for _ in range(size)]
    return lst

def Creat_max_and_min_num():
    max_or_min = randint(-15, 15)
    return max_or_min

def Finding_index(arr, maxim, minim):
    lis = []
    for i in range(len(arr)):
        if minim <= arr[i] <= maxim:
            lis.append(i)
    return lis

