import pytest
from testtomindbox.figures_area import Area

def test_area_higer_0():
    area = Area(fig_type = 'circle', r = -1)

    assert area.calculate_area() > 0


def test_area_circle():
    area = Area(fig_type = 'circle', r = 4)

    assert area.calculate_area() == 50.27


def test_area_triangle():
    area = Area(fig_type = 'triangle', a = 6, b = 6, c = 6)

    assert area.calculate_area() == 15.59


def test_isrec_triangle_false():
    area = Area(fig_type = 'triangle', is_rect = 'is_rectangular', a = 6, b = 6, c = 6)

    assert area.calculate_area() == False


def test_isrec_triangle_true():
    area = Area(fig_type = 'triangle', is_rect =  'is_rectangular', a = 3, b = 4, c = 5)

    assert area.calculate_area() == True


def test_circle_typeerror():
    with pytest.raises(TypeError):
            Area(fig_type ='circle', r = 'some_str').calculate_area()


def test_circle_typeerror():
    with pytest.raises(TypeError):
            Area(fig_type = 'circle').calculate_area()

def test_triangle_typeerror():
    with pytest.raises(TypeError):
            Area(fig_type = 'triangle', a = 1, b = 2).calculate_area()

def test_triange_typeerror():
    with pytest.raises(TypeError):
            Area(fig_type = 'triangle', r = 'some_str', is_rect = 'another_str', a = 1, b = 1).calculate_area()


def test_none_return():
    area = Area(fig_type = 'not triangle and not circle', a = 1,  r = 'sometring')

    assert area.calculate_area() == None

