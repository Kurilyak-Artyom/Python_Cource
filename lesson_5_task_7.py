"""
Создать  вручную  и  заполнить  несколькими  строками  текстовый  файл,  в  котором  каждая 
строка  будет  содержать  данные  о  фирме:  название,  форма  собственности,  выручка, 
издержки.  

Пример строки файла: firm_1   ООО   10000   5000.

Необходимо  построчно  прочитать  файл,  вычислить  прибыль  каждой  компании,  а  также 
среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её ​не включать.​ 

Далее  реализовать  список.  Он  должен  содержать  словарь  с  фирмами  и  их  прибылями,  а 
также  словарь  со  средней  прибылью.  Если  фирма  получила  убытки,  также  добавить  её  в 
словарь (со значением убытков).  

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. 

Итоговый список сохранить в виде json-объекта в соответствующий файл. 

Пример json-объекта: 

[{"​firm_1":​ ​5000,​ "​firm_2":​ ​3000,​ "​firm_3":​ ​1000}​, {"​average_profit":​ ​2000}​] 

"""

from json import dump
from pathlib import Path

the_path = Path(Path.cwd(), 'test_data', 'data7.txt')
the_path_2 = Path(Path.cwd(), 'test_data', 'result7.txt')

profit_making_firms = {}
firms_with_losses = {}
average_profit = {}
result_list = []
profit_making_firms_count = 0
profit_sum = 0

with open(the_path, 'r', encoding='utf-8') as f_obj:
    for line in f_obj:
        if int(line.split()[2]) >= int(line.split()[3]):
            profit_making_firms.update({line.split()[0]: int(line.split()[2]) - int(line.split()[3])})
            profit_making_firms_count += 1
            profit_sum += int(line.split()[2]) - int(line.split()[3])
        else:
            firms_with_losses.update({line.split()[0]: int(line.split()[3]) - int(line.split()[2])})

try:
    average_profit.update({"average_profit": f"{profit_sum / profit_making_firms_count:.2f}"})
except ZeroDivisionError:
    average_profit.update({"average_profit": f"There are no profit making firms!"})

if len(profit_making_firms) > 0:
    result_list.append(profit_making_firms)
if len(firms_with_losses) > 0:
    result_list.append(firms_with_losses)
result_list.append(average_profit)

with open(the_path_2, 'w', encoding='utf-8') as f_obj_2:
    dump(result_list, f_obj_2)

