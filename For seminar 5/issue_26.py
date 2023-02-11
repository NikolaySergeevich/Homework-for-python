num = int(input('Введите число: '))
step = int(input('Введите степень: '))

def rec(n, st):
    if st == 1:
        return n
    return n * rec(n, st -1)