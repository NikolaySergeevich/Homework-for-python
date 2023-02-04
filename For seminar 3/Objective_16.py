# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
from random import randint

def Creat_List_num ():
    num = int(input('Введите размер листа: '))
    list = []
    i = 0
    while i < num:
        list.append(randint(0,10))
        i += 1
    return list

def Finding_num_in_list(list):
    num_person = int(input('Введите число, и программа проверит, сколько раз оно встречается в списке чисел, если оно там есть: '))
    if num_person in list:
        return num_person
    else:
        print('Введённого числа нет в списке')
        # Finding_num_in_list(list)
        exit()

def Count_num_in_lsit(list, num_person):
    count = 0
    for i in list:
        if num_person == i:
            count += 1
        else:
            count
    print(f'Число {num_person} встречается в листе {count} раз')