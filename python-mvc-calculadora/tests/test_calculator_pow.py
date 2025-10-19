# tests/test_calculator_pow.py
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import pytest

from src.model.calculator import Calculator, ExponenteInvalidoError


@pytest.fixture
def calc():
    return Calculator()


def test_potenciacion_casos_base(calc):
    assert calc.potenciacion(0, 0) == 1  # convenio
    assert calc.potenciacion(5, 0) == 1
    assert calc.potenciacion(0, 5) == 0
    assert calc.potenciacion(2, 1) == 2


def test_potenciacion_general(calc):
    assert calc.potenciacion(2, 5) == 32
    assert calc.potenciacion(-2, 5) == -32
    assert calc.potenciacion(-2, 6) == 64
    assert calc.potenciacion(3, 4) == 81


def test_potenciacion_exponente_invalido(calc):
    with pytest.raises(ExponenteInvalidoError):
        calc.potenciacion(2, -1)