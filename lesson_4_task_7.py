"""
Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. 
При вызове функции должен создаваться объект-генератор. 

Функция вызывается следующим образом: for el in fact(n). 
О
на отвечает за получение факториала числа. 
В цикле нужно выводить только первые n чисел, начиная с 1! и до n!.
"""

from math import factorial


def fact(number):
    fact_list = [factorial(i) for i in range(1, number + 1)]
    yield fact_list


print("Enter N: ", end='')
n = int(input())

for el in fact(n):
    print(el)