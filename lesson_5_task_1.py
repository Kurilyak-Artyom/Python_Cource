"""
Создать  программный  файл  в  текстовом  формате,  записать  в  него  построчно  данные, вводимые  пользователем.  
Об  окончании  ввода  данных  будет  свидетельствовать  пустая строка. 
"""

from pathlib import Path

the_path = Path(Path.cwd(), 'test_data','docs.txt')

f_obj = open(the_path, 'w')
cur_string = 'data'

while cur_string != '':
    cur_string = input('Enter new string: ')
    f_obj.write(cur_string + '\n')

f_obj.close()

