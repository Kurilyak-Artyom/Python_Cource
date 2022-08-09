"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. 
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""

def simple_division(the_divident, the_divisor):
    try:
        return f"\n{the_divident}\{the_divisor} = {the_divident / the_divisor:.4f}"
    except ZeroDivisionError:
        return "\nDevision by zero!"


divident = int(input('Enter divident: '))
divisor = int(input('Enter divisor: '))
print(simple_division(divident, divisor))





