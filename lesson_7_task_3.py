class Cell:

    def __init__(self, nucleus_number):
        self.nucleus_number = nucleus_number

    def __str__(self):
        return str(self.nucleus_number)

    def __add__(self, other):
        return Cell(self.nucleus_number + other.nucleus_number)

    def __sub__(self, other):
        if self.nucleus_number - other.nucleus_number > 0:
            return Cell(self.nucleus_number - other.nucleus_number)
        else:
            print("Разница отрицательная. Выполнение операции невозможно!")

    def __mul__(self, other):
        return Cell(self.nucleus_number * other.nucleus_number)

    def __floordiv__(self, other):
        return Cell(int(self.nucleus_number // other.nucleus_number))

    # Используем статический метод, чтобы не было первого обязательного аргумента SELF
    @staticmethod
    def make_order(cell_obj, nucleus_number_in_line):
        order_list = ['*' * nucleus_number_in_line for i in
                      range(int(cell_obj.nucleus_number // nucleus_number_in_line))]
        if int(cell_obj.nucleus_number % nucleus_number_in_line) > 0:
            order_list.append('*' * int(cell_obj.nucleus_number % nucleus_number_in_line))
        return '\n'.join(order_list)


# ================================================================================================================

cell_1 = Cell(2)
cell_2 = Cell(3)
cell_3 = Cell(24)

cell_4 = cell_1 + cell_2
print(cell_4)
print(type(cell_4), '\n')

cell_5 = cell_3 * cell_2
print(cell_5)
print(type(cell_5), '\n')

cell_6 = cell_3 // cell_1
print(cell_6)
print(type(cell_6), '\n')

cell_7 = cell_2 - cell_1
print(cell_7)
print(type(cell_7), '\n')

cell_8 = cell_2 - cell_3
print(cell_8)

print('\n=================================================================\n')

cell_10 = Cell(32)
str_10 = Cell.make_order(cell_10, 7)
print(str_10)






