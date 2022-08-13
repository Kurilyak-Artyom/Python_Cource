"""
итератор, генерирующий целые числа, начиная с указанного;

Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Предусмотрите условие его завершения.
"""

from itertools import count

start_gen = 3
end_gen = 15
gen_list = []

for i in count(start_gen):
    gen_list.append(i)
    if i > end_gen:
        break

print(gen_list)