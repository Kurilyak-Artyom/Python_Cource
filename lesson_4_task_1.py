"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника. 
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. 
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hourly_rate, hours_in_month, bonus = argv

try:
    print(f"Employee salary: {int(hourly_rate) * int(hours_in_month) + int(bonus)}") 
except:
    print("Invalid format of options! Try again")