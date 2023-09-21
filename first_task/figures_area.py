import math
from typing import Union
import pytest


# Класс для круга и метод вычисления его площади
class Circle:
    def __init__(self, params):
        self.r = params.get('r')

    def get_area(self):
        return round(math.pi*self.r ** 2, 2)
    

# Класс для треугольника. Принимает длины сторон
class Triangle:
    def __init__(self, params):
        self.a = params.get('a')
        self.b = params.get('b')
        self.c = params.get('c')
        self.check_rect = params.get('check_rect')
        if self.check_rect == None:
            self.check_rect = False

# Получение площади по формуле Герона
    def get_area(self):
        p = (self.a+self.b+self.c) / 2
        sq = round((p*(p-self.a)*(p-self.b)*(p-self.c)) ** (1 / 2), 2)
        if self.check_rect:
            return sq, self.is_rectangular()
        else:
            return sq
    
# Проверка на прямоугольный треугольник с ограниченной точностью
    def is_rectangular(self):
        EPS = 0.0001
        is_c = self.a ** 2 + self.b ** 2 - self.c ** 2 < EPS
        is_a = self.c ** 2 + self.b ** 2 - self.a ** 2 < EPS
        is_b = self.a ** 2 + self.c ** 2 - self.b ** 2 < EPS

        if is_a or is_b or is_c:
            return True
        else:
            return False


# Основной класс пакета, его следует имортировать
class Area:
    def __init__(self, **kwargs):
        self.type = kwargs.get('fig_type')
        self.params = kwargs
    # Функция вычисления площади и проверку на прямоугольный треугольник
    def calculate_area(self):
        if self.type == 'circle':
            return Circle(self.params).get_area()
        elif self.type == 'triangle':
                return Triangle(self.params).get_area()
        else:
            raise ValueError('Unexpected figure')





