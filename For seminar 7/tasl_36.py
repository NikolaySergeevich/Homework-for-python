# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36 

num_row = int(input('Введите кол-во строк: '))
num_col = int(input('Введите кол-во столбцов: '))

operation = lambda x, y: print(f'элемент по номеру строки и столбца = {x*y}')

def print_operation_table(oper, num_r, num_c):
    for i in range(1, num_r + 1):
        for j in range(1, num_c + 1):
            print(i*j, end=' ')
        print()
    num_x = int(input('Введите номер строки: '))
    num_y = int(input('Введите номер столбца: '))
    oper(num_x, num_y)

print_operation_table(operation,num_row,num_col)






