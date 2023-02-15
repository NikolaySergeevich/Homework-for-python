import task_30 as t30
import task_32 as t32
# -------------------------Задача 30
'''
num_1 = int(input('Введите первый элемент: '))
raz = int(input('Введите разность между 2 соседними элементами: '))
size = int(input('Введите размер списка: '))
lst = []
t30.Creat_lst_of_condition(lst, num_1, raz, size)
'''
# --------------------------Задача 32

lst_start = t32.Creat_lst()
print(lst_start)

max = t32.Creat_max_and_min_num()
min = t32.Creat_max_and_min_num()
print(max, min, sep=', ')

result_lst = t32.Finding_index(lst_start, max, min)
print(result_lst)
