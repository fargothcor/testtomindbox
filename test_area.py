import pytest
from .figures_area import Area

def test_area_higer_0():
    area = Area(fig_type = 'circle', r = -1)

    assert area.calculate_area() > 0


def test_area_circle():
    area = Area('circle', 4)

    assert area.calculate_area() == 50.27


def test_area_triangle():
    area = Area('triangle', 6, 6, 6)

    assert area.calculate_area() == 15.59


def test_isrec_triangle_false():
    area = Area('triangle', 'is_rectangular', 6, 6, 6)

    assert area.calculate_area() == False


def test_isrec_triangle_true():
    area = Area('triangle', 'is_rectangular', 3, 4, 5)

    assert area.calculate_area() == True


def test_circle_typeerror():
    with pytest.raises(TypeError):
            Area(fig_type ='circle', r = 'some_str').calculate_area()


def test_circle_indexerror():
    with pytest.raises(IndexError):
            Area('circle').calculate_area()

def test_triangle_indexerror():
    with pytest.raises(IndexError):
            Area('triangle', 1, 2).calculate_area()

def test_triange_typeerror():
    with pytest.raises(TypeError):
            Area('triangle', 'some_str', 'another_str', 1, 1).calculate_area()


def test_none_return():
    area = Area('not triangle and not circle', 1, 'sometring')

    assert area.calculate_area() == None

