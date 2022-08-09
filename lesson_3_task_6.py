"""
Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же, 
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
"""

def int_func(new_string):
   return new_string.capitalize()

cur_string = input('Enter new string: ')
print(int_func(cur_string))
