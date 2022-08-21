"""
Реализовать базовый класс Worker (работник).

    ● определить атрибуты: name, surname, position (должность), income (доход);
    ● последний атрибут должен быть защищённым и ссылаться на словарь, содержащий
      элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
    ● создать класс Position (должность) на базе класса Worker;
    ● в классе Position реализовать методы получения полного имени сотрудника
      (get_full_name) и дохода с учётом премии (get_total_income);
    ● проверить работу примера на реальных данных: создать экземпляры класса Position,
      передать данные, проверить значения атрибутов, вызвать методы экземпляров.

"""

class Worker():
    _income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        print(f"\nWorker name: {self.name}\nWorker surname: {self.surname}\n")

    def get_total_income(self):
        print("Worker total income: ", self._income["wage"] + self._income["bonus"])


a = Position('Ivan', 'Ivanov', 'HR-manager', 3000, 500)
a.get_full_name()
a.get_total_income()

worker_name = input('Enter worker name: ')
worker_surname = input('Enter worker surname: ')
worker_position = input('Enter worker position: ')
worker_wage = int(input('Enter worker wage: '))
worker_bonus = int(input('Enter worker bonus: '))

a2 = Position(worker_name, worker_surname, worker_position, worker_wage, worker_bonus)
a2.get_full_name()
a2.get_total_income()