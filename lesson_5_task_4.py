"""
Создать (не программно) текстовый файл со следующим содержимым:
 
One — 1 
Two — 2 
Three — 3 
Four — 4 

Напишите программу, открывающую файл на чтение и считывающую построчно данные. 
При этом  английские  числительные  должны  заменяться  на  русские.  
Новый  блок  строк  должен записываться в новый текстовый файл. 

"""

from pathlib import Path

the_path = Path(Path.cwd(), 'test_data', 'data4.txt')
the_path_2 = Path(Path.cwd(), 'test_data', 'result_data4.txt')

input_f_obj = open(the_path, 'r')
output_f_obj = open(the_path_2, encoding='utf-8')
change_srt = {1: "Один", 2: "Два", 3: "Три", 4: "Четыре"}

for line in input_f_obj:
    output_f_obj.write(change_srt[int(line.split()[2])] + '-' + line.split()[2] + '\n')

input_f_obj.close()
output_f_obj.close()
