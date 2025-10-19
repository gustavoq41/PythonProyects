# tests/test_calculator_add_sub.py
import os
import sys

# Asegurar import desde src/
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.model.calculator import Calculator


def test_suma_basica():
    c = Calculator()
    assert c.suma(2, 3) == 5
    assert c.suma(-2, 3) == 1
    assert c.suma(-2, -3) == -5
    assert c.suma(0, 0) == 0


def test_resta_basica():
    c = Calculator()
    assert c.resta(5, 3) == 2
    assert c.resta(-2, 3) == -5
    assert c.resta(-2, -3) == 1
    assert c.resta(0, 7) == -7
