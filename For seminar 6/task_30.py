# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: 
# An= A1 + (n-1) * d.
# Каждое число вводится с новой строки.



def Creat_lst_of_condition(lis, number_1, rz, siz):
    for i in range(1, siz + 1):
        lis.append(number_1 + (i - 1) * rz)
    print(lis)
