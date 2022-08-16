"""
Создать  текстовый  файл  (не  программно),  сохранить  в  нём  несколько  строк,
выполнить подсчёт строк и слов в каждой строке.
"""

from pathlib import Path

the_path = Path(Path.cwd(), 'test_data','data2.txt')

f_obj = open(the_path, 'r')
line_number = 1

for line in f_obj:
    if line == '\n':
        print(f"String №{line_number} is empty!")
        line_number += 1
        continue
    print(f"String №{line_number}: count of words is {len(line.split())}")
    line_number += 1

print(f"\nThere are {line_number - 1} strings in this file.")
f_obj.close()
