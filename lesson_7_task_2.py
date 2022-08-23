"""
Реализовать проект расчёта суммарного расхода ткани на производство одежды. 
Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название. 

К типам одежды в этом проекте относятся пальто и костюм. 

У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). 
Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). 

Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. 

Проверить на практике полученные на этом уроке знания: 

1) реализовать абстрактные классы для основных классов проекта
2) проверить на практике работу декоратора @property.

"""

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, item_count):
        self.the_consumption = 0
        self.item_count = item_count

    @abstractmethod
    def count_consumption(self):
        pass

    # Реализация общего подсчета ткани на один из типов одежды определенного размера
    @property
    def total_consumption(self):
        return self.the_consumption * self.item_count


#########################################################################################

class Coat(Clothes):

    def __init__(self, item_count, V):
        super().__init__(item_count)
        self.V = V

    @property
    def V(self):
        return self.__V

    # Проверяем допустимые значения размера: от 42 до 54
    @V.setter
    def V(self, V):
        if V < 42:
            self.__V = 42
        elif V > 54:
            self.__V = 54
        else:
            self.__V = V

    @property
    def count_consumption(self):
        self.the_consumption = float('{:.2f}'.format(self.V / 6.5 + 0.5))
        print(f"Расход ткани на пальто: {self.the_consumption}\n")


#########################################################################################

class Suit(Clothes):

    def __init__(self, item_count, H):
        super().__init__(item_count)
        self.H = H

    @property
    def H(self):
        return self.__H

    # Проверяем допустимые значения роста: от 150см до 220см
    @H.setter
    def H(self, H):
        if H < 150:
            self.__H = 150
        elif H > 220:
            self.__H = 220
        else:
            self.__H = H

    @property
    def count_consumption(self):
        self.the_consumption = float('{:.2f}'.format(self.H * 2 + 0.3))
        print(f"Расход ткани на костюм: {self.the_consumption}\n")


#########################################################################################

item_1 = Coat(42, 66)
item_1.count_consumption

item_2 = Suit(57, 134)
item_2.count_consumption

print(f"Total consumption is: {(item_1.total_consumption + item_2.total_consumption):.2f}")

