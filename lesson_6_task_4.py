"""
Реализуйте базовый класс Car.

    ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
      А также методы: go, stop, turn(direction), которые должны сообщать, что машина
      поехала, остановилась, повернула (куда);
    ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
    ● добавьте в базовый класс метод show_speed, который должен показывать текущую
      скорость автомобиля;
    ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
      скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
      превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
выведите результат. Вызовите методы и покажите результат.

"""

from random import randint


class Car():

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("\nCar is moving!\n")

    def stop(self):
        print("\nCar has stopped!\n")

    def turn(self):
        print("\nCar has turned!\n")

    def show_speed(self):
        print(f"\nCar is moving with speed {randint(1, self.speed + 1)}")


class TownCar(Car):

    def show_speed(self):
        cur_speed = randint(1, self.speed + 1)
        if cur_speed > 60:
            print(f"\nOver speed!")
        else:
            print(f"\nCar is moving with speed {cur_speed}")


class SportCar(Car):
    def get_info():
        print("This is Sport Car!")


class WorkCar(Car):

    def show_speed(self):
        cur_speed = randint(1, self.speed + 1)
        if cur_speed > 40:
            print(f"\nOver speed!")
        else:
            print(f"\nCar is moving with speed {cur_speed}")


class PoliceCar(Car):
    def get_info():
        print("This is Police Car!")


car1 = TownCar('Model_1', 'Red', 150, False)
print(f"\nCar №1 model: {car1.name}\nCar №1 max speed: {car1.speed}\nCar №1 color: {car1.color}")
car1.show_speed()
car1.turn()

print('======================================================================')

car2 = SportCar('Model_2', 'Green', 250, False)
print(f"\nCar №2 max speed: {car2.speed}\nCar №2 color: {car2.color}\nCar №2 is Police? - {car2.is_police}")
car2.stop()
car2.turn()
car2.get_info()

print('======================================================================')

car3 = WorkCar('Model_3', 'Black', 80, False)
print(f"\nCar №3 max speed: {car3.speed}\nCar №3 color: {car3.color}")
car3.show_speed()
car3.stop()

print('======================================================================')

car4 = PoliceCar('Police car', 'Silver', 300, True)
print(f"\nCar №4 max speed: {car4.speed}\nCar №4 color: {car4.color}\nCar №4 is Police? - {car4.is_police}")
car4.stop()
car4.turn()
car4.get_info()








