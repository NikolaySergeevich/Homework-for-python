# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.


def Creat_list(size):
    lstt_1 = []
    for i in range(size):
        num_1 = int(input('Введите значение: '))
        lstt_1.append(num_1)
    return lstt_1

def Revers_in_mnosh(lst):
    mnosh = set()
    for i in lst:
        mnosh.add(i)
    return mnosh

def Intersection(mnosh_1, mnosh_2):
    result = mnosh_1.intersection(mnosh_2)
    return result