"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
"""

def the_sum(arg1, arg2, arg3):
    l = []
    l.append(arg1)
    l.append(arg2)
    l.append(arg3)
    l.sort()
    return l[1] + l[2]

arg_1 = int(input('Enter argument №1: '))
arg_2 = int(input('Enter argument №2: '))
arg_3 = int(input('Enter argument №3: '))

print(f"\nResult: {the_sum(arg_1, arg_2, arg_3)}")
