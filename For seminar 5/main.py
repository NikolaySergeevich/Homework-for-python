from issue_26 import *
from issue_28 import *
# --------------- Issue 26
num = int(input('Введите число: '))
step = int(input('Введите степень: '))
print(f'Число {num} в степени {step} будет = {rec(num, step)}')
print()
# --------------- Issue 28
num_1 = int(input('введите первое число: '))
num_2 = int(input('введите второе число: '))
print(f'Сумма {num_1} и {num_2} равна {sum(num_1, num_2, cou = 0)}')