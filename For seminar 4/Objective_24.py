# : В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.


from random import randint
def Creat_gruda():
    count_kust = randint(6, 8)
    gryda = [randint(4, 20) for _ in range(count_kust)]
    return gryda

def Result(gruda_list):
    number_cysta = 0 
    max = gruda_list[0] + gruda_list[1] + gruda_list[-1]
    max_i = 0
    for i in gruda_list:
        gruda_list.insert(0, gruda_list.pop())
        if gruda_list[0] + gruda_list[1] + gruda_list[-1] > max:
            max = gruda_list[0] + gruda_list[1] + gruda_list[-1]
            number_cysta += 1
            max_i = number_cysta
        else:
            number_cysta += 1
    if len(gruda_list) - max_i == len(gruda_list):
        max_i = 0
    else:
        max_i = len(gruda_list) - max_i
    print(f'{max} - это максимальное кол-во ягод, если модуль подъедет к {max_i} кусту.\n\
        На ферме грядки нумеруются с нуля')
    return max_i

