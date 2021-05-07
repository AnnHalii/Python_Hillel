import math


class Shape:
    def calc_perimeter(self):
        raise NotImplementedError

    def calc_space(self):
        raise NotImplementedError

    def get_info(self):
        print(f'Площадь = {self.calc_space()}, периметр = {self.calc_perimeter()}')


class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def calc_perimeter(self):
        return self.x*2 + self.h*2

    def calc_space(self):
        return self.x*self.y


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calc_perimeter(self):
        return self.a + self.b + self.c

    def calc_space(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))


class Square(Shape):
    def __init__(self, a):
        self.a = a

    def calc_perimeter(self):
        return self.a*4

    def calc_space(self):
        return self.a**2


pr = Rectangle(5, 5, 10, 10)
pr.get_info()
tr = Triangle(2, 4, 3)
tr.get_info()
sq = Square(2)
sq.get_info()


# class Square:
#     def __init__(self, s):
#         self.__side = s
#         self.__area = None
#
#     @property
#     def side(self):
#         return self.__side
#
#     @side.setter
#     def side(self, value):
#         self.__side = value
#         self.__area = None
#
#     @property
#     def area(self):
#         if self.__area is None:
#             print('calculate area')
#             self.__area = self.__side**2
#         return self.__area
#
#
# r = Square(4)
# print(r.area)
# print(r.area)
