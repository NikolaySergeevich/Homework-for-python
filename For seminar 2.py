# ------------------Задача 10: 
# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть
'''
from random import randint
num = randint(1,20)
i = 1
orel = 0
reshca = 0
if num == 1:
    print(num)
    print('Есть только одна мотена, так что переворачивать ничего не нужно')
else:
    while i <= num:
        from random import randint
        mon = randint(0,1)
        print(mon, end=', ')
        i += 1
        if mon == 1:
            orel += 1
        else:
            reshca += 1
    if orel >= reshca:
        print('\n'f"нужно перевернуть {reshca} монет")
    else:
        print('\n'f"нужно перевернуть {orel} монет")
'''

# --------------------Задача 12: 
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
'''
import math
from random import randint
num_1 = randint(0,1000)
from random import randint
num_2 = randint(0,1000)

sum = num_1 + num_2
proz = num_1 * num_2
print(f'Сумма загаданых чисел = {sum}')
print(f'Произведение загаданых чисел = {proz}')

D = sum**2 - 4 * -1 * -proz
print(f'дискрименант =  {D}')
sqrt_D = int(math.sqrt(D))
print(f'Корень из {D} = {sqrt_D}' )

if D < 0:
    print('Нет решения')
elif D > 0:
    result_1 = ((-sum) + sqrt_D) // (-2)
    result_2 = ((-sum) - sqrt_D) // (-2)
    print(f'загаданы {result_1} и {result_2}')
else:
    result_1 = -sum // 2 * -proz
    result_2 = sum - result_1

'''

# ------------------------Задача 14: 
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.
from random import randint
num_1 = randint(0,1000)
i = 0
while True:
    res = 2**i
    if res <= num_1:
        print(res, end= ', ')
        i +=1
    else:
        break
print(f'вывести все целые степени двойки, не превосходящие числа {num_1}')
