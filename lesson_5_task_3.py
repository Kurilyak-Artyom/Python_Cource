"""
Создать  текстовый  файл  (не  программно).  Построчно  записать  фамилии  сотрудников  и 
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода 
сотрудников.

Пример файла:

Иванов 23543.12 
Петров 13749.32 
"""

from pathlib import Path

the_path = Path(Path.cwd(), 'test_data', 'data3.txt')

f_obj = open(the_path, 'r', encoding='utf-8')
staff_count = 0
salary_sum = 0

for line in f_obj:
    staff_count += 1
    salary_sum += float(line.split()[1])
    if float(line.split()[1]) < 20000:
        print(f"Сотрудник {line.split()[0]} имеет оклад менее 20 тысяч!\n")

print(f"Средний оклад сотрудников равен {salary_sum / staff_count:.2f}")
f_obj.close()


