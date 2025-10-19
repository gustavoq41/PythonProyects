# tests/test_calculator_mul_div_mod.py
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest

from src.model.calculator import Calculator, DivisionPorCeroError


@pytest.fixture
def calc():
    return Calculator()


def test_multiplicacion_signos(calc):
    assert calc.multiplicacion(3, 4) == 12
    assert calc.multiplicacion(-3, 4) == -12
    assert calc.multiplicacion(3, -4) == -12
    assert calc.multiplicacion(-3, -4) == 12
    assert calc.multiplicacion(0, 99) == 0


def test_division_basica(calc):
    assert calc.division(12, 3) == 4
    assert calc.division(13, 3) == 4  # truncado hacia 0
    assert calc.division(-13, 3) == -4
    assert calc.division(13, -3) == -4
    assert calc.division(-13, -3) == 4
    assert calc.division(0, 5) == 0


def test_division_por_cero(calc):
    with pytest.raises(DivisionPorCeroError):
        calc.division(5, 0)


def test_modulo_basico(calc):
    # Resto con mismo signo del dividendo
    assert calc.modulo(7, 3) == 1
    assert calc.modulo(-7, 3) == -1
    assert calc.modulo(7, -3) == 1
    assert calc.modulo(-7, -3) == -1
    assert calc.modulo(0, 5) == 0


def test_modulo_por_cero(calc):
    with pytest.raises(DivisionPorCeroError):
        calc.modulo(5, 0)
