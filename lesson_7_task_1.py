"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), 
который должен принимать данные (список списков) для формирования матрицы.

Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31    32         3    5    32        3    5    8    3
37    43         2    4    6         8    3    7    1
51    86        -1   64   -8

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
"""

class Matrix:

    def __init__(self, *args):
        self.the_matrix = list(*args)

    def prepare_line(self, the_list):
        return '\t\t'.join(str(el) for el in the_list)

    def __str__(self):
        return '\n'.join(self.prepare_line(el) for el in self.the_matrix)

    def check_size(self, other):
        if len(self.the_matrix) == len(other.the_matrix) and len(self.the_matrix[0]) == len(other.the_matrix[0]):
            return True
        else:
            return False

    def __add__(self, other):
        if self.check_size(other):
            return Matrix([[self.the_matrix[i][j] + other.the_matrix[i][j] for j in range(len(self.the_matrix[0]))]
                           for i in range(len(self.the_matrix))])
        else:
            print("Невозможно сложение матриц разного размера!")


first_matrix = [[122, 2, 3], [4, 571, 6], [7, 8, 9]]
second_matrix = [[10, -20, 1], [40, -5, 1], [70, 80, 100]]

m1 = Matrix(first_matrix)
print(f"First matrix:\n{m1}\n")

m2 = Matrix(second_matrix)
print(f"Second matrix:\n{m2}\n")

m3 = m1 + m2
print(f"M1 + M2:\n{m3}\n")
print(type(m3))




