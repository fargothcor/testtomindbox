import math
from typing import Union
import pytest

class Circle:
    def __init__(self, r):
        self.r = r


    def get_area(self):
        return round(math.pi*self.r ** 2, 2)
    

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def get_area(self):
        p = (self.a+self.b+self.c) / 2
        return round((p*(p-self.a)*(p-self.b)*(p-self.c)) ** (1 / 2), 2)
    
    def is_rectangular(self):
        eps = 0.0001
        is_c = self.a ** 2 + self.b ** 2 - self.c ** 2 < eps
        is_a = self.c ** 2 + self.b ** 2 - self.a ** 2 < eps
        is_b = self.a ** 2 + self.c ** 2 - self.b ** 2 < eps

        if is_a or is_b or is_c:
            return True
        else:
            return False

class Area:
    def __init__(self, fig_type: str = '', r: Union[float, int] = 0, \
                is_rect : str = None, a: Union[float, int] = 0, b: \
                Union[float, int] = 0, c: Union[float, int] = 0):
        self.type = fig_type
        self.r = r
        self.a = a
        self.b = b
        self.c = c
        self.is_rect = is_rect

    
    def calculate_area(self):
        if self.type == 'circle':
            return Circle(self.r).get_area()
        elif self.type == 'triangle':
            if self.is_rect == 'is_rectangular':
                return Triangle(self.a, self.b, self.c).is_rectangular()
            else:
                return Triangle(self.a, self.b, self.c).get_area()
        else:
            return None






