"""
Реализовать класс Road (дорога).

    ● определить атрибуты: length (длина), width (ширина);
    ● значения атрибутов должны передаваться при создании экземпляра класса;
    ● атрибуты сделать защищёнными;
    ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
    ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
      дороги асфальтом, толщиной в 1 см*число см толщины полотна;
    ● проверить работу метода.

    Например: 20 м*5000 м*25 кг*5 см = 12500 т.

"""

class Road():

    def __init__(self, the_length, the_weight):
        self._length = the_length
        self._weight = the_weight

    def asphalt_mass_calculation(self, mass_of_asphalt_per_square_meter, coating_thickness):
        print(
            f"\nRequired mass of asphalt: {self._length * self._weight * mass_of_asphalt_per_square_meter * coating_thickness} tons")


the_length = int(input('Enter road length: '))
the_weight = int(input('Enter road weight: '))

the_mass_per_square_meter = int(input('Enter mass of asphalt per 1 square meter: '))
the_coating_thickness = int(input('Enter coating thickness: '))

a = Road(the_length, the_weight)
a.asphalt_mass_calculation(the_mass_per_square_meter, the_coating_thickness)


