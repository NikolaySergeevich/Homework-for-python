
import Objective_22 as Obj_22
# --------------22 Задача

size_1 = int(input('Введите размер первого множества: '))
print('Сейчас вам предложат ввести значения для этого множества')
lst_1 = Obj_22.Creat_list(size_1)

size_2 = int(input('Введите размер второго множества: '))
print('Сейчас вам предложат ввести значения для этого множества')
lst_2 = Obj_22.Creat_list(size_2)

print(lst_1)
print(lst_2)
print()
mnosh_1 = Obj_22.Revers_in_mnosh(lst_1)
mnosh_2 = Obj_22.Revers_in_mnosh(lst_2)
mnosh = Obj_22.Intersection(mnosh_1, mnosh_2)
print(mnosh)

mnosh = list(mnosh)
mnosh.sort()
print(mnosh)

