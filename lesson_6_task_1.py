"""
Создать класс TrafficLight (светофор).
    ● определить у него один атрибут color (цвет) и метод running (запуск);
    ● атрибут реализовать как приватный;
    ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
      зелёный;
    ● продолжительность первого состояния (красный) составляет 7 секунд, второго
      (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
    ● переключение между режимами должно осуществляться только в указанном порядке
      (красный, жёлтый, зелёный);
    ● проверить работу примера, создав экземпляр и вызвав описанный метод.

"""

import time


class traffic_lights:
    __color = ''

    def running(self):
        self.__color = 'RED'
        print(f"Current light is {self.__color}")
        time.sleep(7)

        self.__color = 'YELLOW'
        print(f"Current light is {self.__color}")
        time.sleep(2)

        self.__color = 'GREEN'
        print(f"Current light is {self.__color}")
        time.sleep(3)

        print()


test_obj = traffic_lights()

itr_number = int(input('Enter iteration number for traffic lights: '))

for i in range(itr_number):
    test_obj.running()


