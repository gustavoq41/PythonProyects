from __future__ import annotations
from src.model.calculator import Calculator, DivisionPorCeroError, ExponenteInvalidoError
from src.view.app_view import AppView


class AppController:
    """Controlador: conecta la Vista con el Modelo."""

    def __init__(self, view: AppView, model: Calculator) -> None:
        self.view = view
        self.model = model
        self.view.set_controller(self)

    # ---------- Handlers básicos ----------

    def _with_operands(self, op_name: str, func) -> None:
        try:
            a, b = self.view.get_operands()
            result = func(a, b)
            self.view.set_result(str(result))
        except (DivisionPorCeroError, ExponenteInvalidoError, ValueError) as e:
            self.view.show_error(str(e))
        except Exception:
            self.view.show_error(f"Ocurrió un error en la operación {op_name}.")

    def _with_single_operand(self, op_name: str, func) -> None:
        try:
            a = self.view.get_single_operand()
            result = func(a)
            self.view.set_result(str(result))
        except ValueError as e:
            self.view.show_error(str(e))
        except Exception:
            self.view.show_error(f"Ocurrió un error en la operación {op_name}.")

    # ---------- Operaciones ----------

    def on_add(self): self._with_operands("suma", self.model.suma)
    def on_sub(self): self._with_operands("resta", self.model.resta)
    def on_mul(self): self._with_operands("multiplicación", self.model.multiplicacion)
    def on_div(self): self._with_operands("división", self.model.division)
    def on_mod(self): self._with_operands("módulo", self.model.modulo)
    def on_pow(self): self._with_operands("potenciación", self.model.potenciacion)
    def on_factorial(self): self._with_single_operand("factorial", self.model.factorial)

    # ---------- Nuevas funciones ----------

    def on_exp(self): self._with_single_operand("exp", self.model.exp)
    def on_cos(self): self._with_single_operand("cos", self.model.cos)
    def on_sin(self): self._with_single_operand("sin", self.model.sin)
    def on_atan(self): self._with_single_operand("atan", self.model.atan)

    def on_pi(self):
        try:
            result = self.model.pi()
            self.view.set_result(str(result))
        except Exception:
            self.view.show_error("Error al calcular π.")
