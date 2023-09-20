import math
from typing import Union
import pytest


# Класс для круга и метод вычисления его площади
class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return round(math.pi*self.r ** 2, 2)
    

# Класс для треугольника. Принимает длины сторон
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

# Получение площади по формуле Герона
    def get_area(self):
        p = (self.a+self.b+self.c) / 2
        return round((p*(p-self.a)*(p-self.b)*(p-self.c)) ** (1 / 2), 2)
    
# Проверка на прямоугольный треугольник с ограниченной точностью
    def is_rectangular(self):
        eps = 0.0001
        is_c = self.a ** 2 + self.b ** 2 - self.c ** 2 < eps
        is_a = self.c ** 2 + self.b ** 2 - self.a ** 2 < eps
        is_b = self.a ** 2 + self.c ** 2 - self.b ** 2 < eps

        if is_a or is_b or is_c:
            return True
        else:
            return False


# Основной класс пакета, его следует имортировать
class Area:
    def __init__(self, fig_type: str = '', r: Union[float, int] = None, \
                check_rect : bool = False, a: Union[float, int] = None, b: \
                Union[float, int] = None, c: Union[float, int] = None):
        self.type = fig_type
        self.r = r
        self.a = a
        self.b = b
        self.c = c
        self.check_rect = check_rect

    # Функция вычисления площади и проверку на прямоугольный треугольник
    def calculate_area(self):
        if self.type == 'circle':
            return Circle(self.r).get_area()
        elif self.type == 'triangle':
            if self.check_rect:
                return Triangle(self.a, self.b, self.c).is_rectangular()
            else:
                return Triangle(self.a, self.b, self.c).get_area()
        else:
            raise ValueError('Unexpected figure')





