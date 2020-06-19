""" the task 1 """
class Matrix:
    def __init__(self,mtr):
        self.mtr = mtr
        self.height = len(mtr)
        if self.height > 0:
            self.width = len(mtr[0])
        else:
            self.width = 0


    def __str__(self):
        my_str = ""
        for row in self.mtr:
            for el in row:
                my_str += str(el) + " "
            my_str += "\n"
        return my_str

    def __add__(self, other):
        if self.height == other.height and self.width == other.width:
            new_mtr = []
            for row_ind, row in enumerate(self.mtr):
                new_row = []
                for col_ind, col_el in enumerate(row):
                    new_row.append(other.mtr[row_ind][col_ind] + col_el)
                new_mtr.append(new_row)
            return Matrix(new_mtr)
        raise ValueError('Не соотвествующие размеры матриц')




m1 = Matrix([[2, 3, 4], [6, 4, 5], [5, 6, 8]])
m2 = Matrix([[5, 2, 3], [1, 6, 1], [6, 9, 3]])
print(m1)
print(m2)
print(m1+m2)


""" the task 2 """
from abc import ABC, abstractmethod

class Сlothes(ABC):

    @abstractmethod
    def сons_tissue(self):
        pass


class Coat(Сlothes):
    def __init__(self, v):
        self.v = v

    @property
    def сons_tissue(self):
        return self.v / 6.5 + 0.5

class Costume(Сlothes):
    def __init__(self, h):
        self.h = h

    @property
    def сons_tissue(self):
        return 2 * self.h + 0.3


c_1 = Coat(3)
print(f"Расход ткани на пальто: {c_1.сons_tissue}")
c_2 = Costume(5)
print(f"Расход ткани на костюм {c_2.сons_tissue}")


""" the task 3 """
class Ceil:
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    def __sub__(self, other):
        return self.size - other.size

    def __mul__(self, other):
        return self.size * other.size

    def __truediv__(self, other):
        return int(self.size / other.size)

    def make_order(self, n):
        my_str = ""
        j = 0
        for i in range(0, self.size):
            my_str += '*'
            j += 1
            if j >= n:
                my_str += "\n"
                j = 0
        return my_str

c_1 = Ceil(12)
c_2 = Ceil(7)

print(c_1 + c_2)
print(c_1 - c_2)
print(c_1 * c_2)
print(c_1 / c_2)
print()
print(c_1.make_order(5))