"""
итератор, повторяющий элементы некоторого списка, определённого заранее;

Подсказка: используйте функцию count() и cycle() модуля itertools. 
Обратите внимание, что создаваемый цикл не должен быть бесконечным. 
Предусмотрите условие его завершения.
"""

from itertools import cycle

start_cycle = 0
cycle_count = 5
the_list = [1, 2, 4, 8]

for el in cycle(the_list):
    print(f"Iterration[{start_cycle + 1}]: {el}")
    if start_cycle > cycle_count:
        break
    start_cycle += 1