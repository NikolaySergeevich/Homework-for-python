# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.


def rec(n, st):
    if st == 0:
        return 1
    if st == 1:
        return n
    return n * rec(n, st - 1)