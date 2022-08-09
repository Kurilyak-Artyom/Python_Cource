"""
Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, 
но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().
"""

def int_func(new_string):
    buf_list = new_string.split()
    for i in range(len(buf_list)):
        buf_list[i] = buf_list[i].capitalize()
    print("\nResult string: ", ' '.join(buf_list))

cur_str = input('Enter new string: ')
int_func(cur_str)
