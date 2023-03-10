# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам

stih = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
fraza =(stih.split())
print(stih)
print(fraza)

def count_glas(tex):  # ищет кло-во гласных в тексте
    count = 0
    glasnue = ['а','е','о','у']
    for i in range(len(tex)):
        if tex[i] in glasnue:
            count += 1
    return count

lst_count_gl = list(map(count_glas, fraza)) # каждый элемент списка будет равным кол-ву гласных в одной фразе

if len(set(lst_count_gl)) == 1:
    print('Парам пам-пам')
else:
    print('Рифмы нет')