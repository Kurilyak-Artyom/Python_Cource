"""
Создать  программный  файл  в  текстовом  формате,  записать  в  него  построчно  данные, вводимые  пользователем.  
Об  окончании  ввода  данных  будет  свидетельствовать  пустая строка. 
"""

f_obj = open(r"D:\test_data\data1.txt", 'w')
cur_string = 'data'

while cur_string != '':
    cur_string = input('Enter new string: ')
    f_obj.write(cur_string + '\n')

f_obj.close()

