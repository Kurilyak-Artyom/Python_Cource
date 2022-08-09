"""
Программа принимает действительное положительное число x и целое отрицательное число y. 
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y). 
При решении задания нужно обойтись без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами. 
Первый — возведение в степень с помощью оператора **. 
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
"""

#1-ый Способ
def my_func1(x, y):
    return x ** y

#2-ой Способ
def my_func2(x, y):
    degree = 1
    result = x
    while degree < y:
        result = result * x
        degree += 1
    return result

the_x = float(input('Enter number: '))
the_y = int(input('Enter degree: '))

result1 = my_func1(the_x, the_y)
result2 = my_func2(the_x, the_y)

print(f"\nBy the first mode: {result1:.2f}\n\nBy the second mode: {result2:.2f}")
