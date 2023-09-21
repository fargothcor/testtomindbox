import pytest
from first_task.figures_area import Area

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
    area = Area(fig_type = 'triangle', check_rect = True, a = 6, b = 6, c = 6)

    assert area.calculate_area() == (15.59, False)


def test_isrec_triangle_true():
    area = Area(fig_type = 'triangle', check_rect =  True, a = 3, b = 4, c = 5)

    assert area.calculate_area() == (6.0, True)


def test_circle_typeerror():
    with pytest.raises(TypeError):
        Area(fig_type ='circle', r = 'some_str').calculate_area()


def test_circle_miss_r():
    with pytest.raises(TypeError):
        Area(fig_type = 'circle').calculate_area()

def test_triangle_typeerror():
    with pytest.raises(TypeError):
        Area(fig_type = 'triangle', a = 1, b = 2).calculate_area()

def test_triange_typeerror():
    with pytest.raises(TypeError):
        Area(fig_type = 'triangle', r = 'some_str', check_rect = 'another_str', a = 1, b = 1).calculate_area()


def test_raise_valueerror():
    with pytest.raises(ValueError):
        Area(fig_type = 'not triangle and not circle', a = 1,  r = 'some_string').calculate_area()


