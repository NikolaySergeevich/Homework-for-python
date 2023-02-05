# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

from random import randint

def Creat_List_num ():
    num = int(input('Введите размер листа: '))
    list = []
    i = 0
    while i < num:
        list.append(randint(-10,20))
        i += 1
    return list

def Close_num (listik):
    listik = list(set(listik)) # Возвращает значения списка без повторящихся значений
    print(listik)
    
    list.sort(listik) 
    print(listik)
    
    num_pers = int(input('Введите число, и программа покажет, какое число из списка самое близкое к вашему: '))
    result_1 = num_pers
    result_2 = num_pers
    if num_pers in listik:
        print(f'Число {num_pers} есть в списке, оно и является ближайшим к себе')
    elif num_pers > listik[-1]:
        print(f'число {listik[-1]} будет самым близким к {num_pers}')
    elif num_pers < listik[0]:
        print(f'число {listik[0]} будет самым близким к {num_pers}')
    else:
        while result_1 not in listik:
            result_1 += 1
        while result_2 not in listik:
            result_2 -= 1
        if result_1 - num_pers == num_pers - result_2:
            print(f'числа {result_1} и {result_2} будут самыми близкими к {num_pers}')
        elif result_1 - num_pers < num_pers - result_2:
            print(f'число {result_1} будет самым близким к {num_pers}')
        else:
            print(f'число {result_2} будет самым близким к {num_pers}')
    