"""
Создать  (программно)  текстовый  файл,  записать  в  него  программно  набор  чисел, разделённых пробелами. 

Программа должна подсчитывать сумму чисел в файле и выводить её на экран. 
"""

from random import randint
from functools import reduce
from pathlib import Path

the_path = Path(Path.cwd(), 'test_data', 'data5.txt')


def the_sum(prev_el, el):
    return int(prev_el) + int(el)


out_f_obj = open(the_path, 'w')
out_f_obj.write(' '.join([str(randint(1, 512)) for i in range(10)]))
out_f_obj.close()

in_f_obj = open(the_path, 'r')
print(reduce(the_sum, in_f_obj.read().split()))
in_f_obj.close()


