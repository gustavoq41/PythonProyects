from __future__ import annotations


class DivisionPorCeroError(Exception):
    """Error al intentar dividir entre cero."""


class ExponenteInvalidoError(Exception):
    """Error cuando el exponente no es un entero válido (esperado >= 0)."""


class Calculator:
    """Implementa operaciones aritméticas enteras bajo restricciones del enunciado.

    Restricciones:
    - No usar: pow, math.*, divmod, %, **, //, abs, round.
    - Solo usar: +, -, comparaciones, bucles, y funciones del mismo modelo.
    """

    # ========= Helpers internos permitidos =========

    def _valor_absoluto(self, n: int) -> int:
        if n < 0:
            return -n
        return n

    def _mismo_signo(self, a: int, b: int) -> bool:
        return (a >= 0 and b >= 0) or (a < 0 and b < 0)

    def _es_par(self, n: int) -> bool:
        m = n
        while m >= 2:
            m = m - 2
        return m == 0

    def _mitad(self, n: int) -> int:
        m = n
        c = 0
        while m >= 2:
            m = m - 2
            c = c + 1
        return c

    # ========= Operaciones básicas =========

    def suma(self, a: int, b: int) -> int:
        return a + b

    def resta(self, a: int, b: int) -> int:
        return a - b

    def multiplicacion(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0

        sign = 1
        if not self._mismo_signo(a, b):
            sign = -1

        x = self._valor_absoluto(a)
        y = self._valor_absoluto(b)

        menor = x if x < y else y
        mayor = y if x < y else x

        acc = 0
        i = 0
        while i < menor:
            acc = acc + mayor
            i = i + 1

        if sign < 0:
            return -acc
        return acc

    def division(self, a: int, b: int) -> int:
        if b == 0:
            raise DivisionPorCeroError("División por cero no definida.")
        if a == 0:
            return 0

        sign = 1
        if not self._mismo_signo(a, b):
            sign = -1

        n = self._valor_absoluto(a)
        d = self._valor_absoluto(b)
        q = 0
        while n >= d:
            temp = d
            mult = 1
            while (n - temp) >= 0 and (n - temp) >= temp:
                temp = temp + temp
                mult = mult + mult
            n = n - temp
            q = q + mult

        if sign < 0:
            return -q
        return q

    def modulo(self, a: int, b: int) -> int:
        if b == 0:
            raise DivisionPorCeroError("Módulo por cero no definido.")
        if a == 0:
            return 0

        sign_a = 1 if a >= 0 else -1
        n = self._valor_absoluto(a)
        d = self._valor_absoluto(b)

        while n >= d:
            temp = d
            while (n - temp) >= 0 and (n - temp) >= temp:
                temp = temp + temp
            n = n - temp

        if sign_a < 0:
            return -n
        return n

    def factorial(self, numero: int) -> int:
        if numero < 0:
            raise ExponenteInvalidoError("Factorial no definido para n < 0.")
        if numero == 0:
            return 1
        acumulador = 1
        indice = 1
        while indice <= numero:
            acumulador = self.multiplicacion(acumulador, indice)
            indice = indice + 1
        return acumulador

    def potenciacion(self, a: int, b: int) -> int:
        if b < 0:
            raise ExponenteInvalidoError("Exponente negativo no soportado.")
        if b == 0:
            return 1
        if a == 0:
            return 0

        base = a
        exp = b
        res = 1
        while exp > 0:
            if not self._es_par(exp):
                res = self.multiplicacion(res, base)
            base = self.multiplicacion(base, base)
            exp = self._mitad(exp)
        return res

    # ========= Series infinitas (aproximaciones) =========

    def exp(self, x: float, n_terms: int = 20) -> float:
        """Serie de Taylor para e^x."""
        result = 0.0
        k = 0
        while k < n_terms:
            # término = x^k / k!
            num = 1.0
            i = 0
            while i < k:
                num *= x
                i += 1
            den = 1
            j = 1
            while j <= k:
                den *= j
                j += 1
            result += num / den
            k += 1
        return result

    def cos(self, x: float, n_terms: int = 20) -> float:
        """Serie de Taylor para cos(x)."""
        result = 0.0
        n = 0
        while n < n_terms:
            num = 1.0
            i = 0
            while i < 2 * n:
                num *= x
                i += 1
            den = 1
            j = 1
            while j <= 2 * n:
                den *= j
                j += 1
            term = ((-1) ** n) * (num / den)
            result += term
            n += 1
        return result

    def sin(self, x: float, n_terms: int = 20) -> float:
        """Serie de Taylor para sin(x)."""
        result = 0.0
        n = 0
        while n < n_terms:
            num = 1.0
            i = 0
            while i < 2 * n + 1:
                num *= x
                i += 1
            den = 1
            j = 1
            while j <= 2 * n + 1:
                den *= j
                j += 1
            term = ((-1) ** n) * (num / den)
            result += term
            n += 1
        return result

    def atan(self, x: float, n_terms: int = 100) -> float:
        """Serie de Taylor para arctan(x), válida para |x| ≤ 1."""
        if x < -1 or x > 1:
            raise ValueError("La serie de arctan(x) converge solo para |x| ≤ 1")
        result = 0.0
        n = 0
        while n < n_terms:
            num = 1.0
            i = 0
            while i < (2 * n + 1):
                num *= x
                i += 1
            term = ((-1) ** n) * (num / (2 * n + 1))
            result += term
            n += 1
        return result

    def pi(self, n_terms: int = 100000) -> float:
        """Fórmula de Leibniz: π/4 = Σ [(-1)^n / (2n+1)]."""
        result = 0.0
        n = 0
        while n < n_terms:
            term = ((-1) ** n) / (2 * n + 1)
            result += term
            n += 1
        return result * 4
