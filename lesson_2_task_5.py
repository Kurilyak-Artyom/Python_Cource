"""
5. Реализовать структуру «Рейтинг», представляющую собой не
возрастающий набор натуральных чисел
(каждый элемент ряда меньше или равен предыдущему).

У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.

Набор натуральных чисел можно задать непосредственно в коде,
например, my_list = [7, 5, 3, 3, 2].
"""

my_list = [12, 9, 9, 9, 7, 5, 3, 3, 2, 1, 1]

while True:
    cur_step = input('Enter next number or \'End\': ')

    #END WHILE
    if cur_step == 'End':
        print(f'{my_list}')
        break

    #NEW ELEMENT ALREADY EXISTS
    if int(cur_step) in my_list:
        my_list.insert(my_list.index(int(cur_step)) + 1, int(cur_step))
        print(f'{my_list}')
        continue

    buf_list = list(set(my_list))[::-1]

    #NEW THE MOST BIG ELEMENT
    if buf_list[0] < int(cur_step):
        my_list.insert(0, int(cur_step))
        print(f'{my_list}')
        continue

    #NEW THE MOST SMALL ELEMENT
    if buf_list[len(buf_list) - 1] > int(cur_step):
        my_list.append(int(cur_step))
        print(f'{my_list}')
        continue

    #LAST CASE
    for i in range(len(buf_list)):
        if int(cur_step) >= buf_list[i]:
            my_list.insert(my_list.index(buf_list[i]), int(cur_step))
            print(f'{my_list}')
            break
