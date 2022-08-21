"""
Реализовать класс Stationery (канцелярская принадлежность).

    ● определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    ● создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    ● в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    ● создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""

class Stationery():

    def __init__(self, title):
        self.title = title

    def drow(self):
        print("Запуск отрисовки!")


class Handle(Stationery):

    def drow(self):
        print(f"Отрисовка при помощи Маркера \"{self.title}\"!")


class Pen(Stationery):

    def drow(self):
        print(f"Отрисовка при помощи Ручки \"{self.title}\"!")


class Pencil(Stationery):

    def drow(self):
        print(f"Отрисовка при помощи Карандаша \"{self.title}\"!")


item_1 = Stationery('New stationary')
item_1.drow()

item_2 = Handle('Яркий красный')
item_2.drow()

item_3 = Pen('Зеленая, шариковая')
item_3.drow()

item_4 = Pencil('Простой карандаш, мягкий')
item_4.drow()


