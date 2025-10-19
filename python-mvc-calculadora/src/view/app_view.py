from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Tuple, Optional


class AppView(tk.Tk):
    """Vista de la aplicación (tkinter)."""

    def __init__(self) -> None:
        super().__init__()
        self.title("Calculadora MVC (Python)")
        self.geometry("900x420")
        self.resizable(False, False)

        self._controller = None  # type: Optional[object]

        frm = tk.Frame(self, padx=12, pady=12)
        frm.pack(fill=tk.BOTH, expand=True)

        tk.Label(frm, text="Operando A:").grid(row=0, column=0, sticky="w")
        tk.Label(frm, text="Operando B:").grid(row=1, column=0, sticky="w")

        self.entry_a = tk.Entry(frm, width=20)
        self.entry_b = tk.Entry(frm, width=20)
        self.entry_a.grid(row=0, column=1, padx=6, pady=4)
        self.entry_b.grid(row=1, column=1, padx=6, pady=4)

        ops = tk.Frame(frm)
        ops.grid(row=2, column=0, columnspan=2, pady=8)

        # Operaciones básicas
        self.btn_add = tk.Button(ops, text="+", width=5)
        self.btn_sub = tk.Button(ops, text="−", width=5)
        self.btn_mul = tk.Button(ops, text="×", width=5)
        self.btn_div = tk.Button(ops, text="÷", width=5)
        self.btn_mod = tk.Button(ops, text="mod", width=5)
        self.btn_pow = tk.Button(ops, text="^", width=5)
        self.btn_fact = tk.Button(ops, text="n!", width=5)

        # Nuevas funciones
        self.btn_exp = tk.Button(ops, text="eˣ", width=5)
        self.btn_cos = tk.Button(ops, text="cos", width=5)
        self.btn_sin = tk.Button(ops, text="sin", width=5)
        self.btn_atan = tk.Button(ops, text="atan", width=5)
        self.btn_pi = tk.Button(ops, text="π", width=5)

        # Distribución
        buttons = [
            self.btn_add, self.btn_sub, self.btn_mul, self.btn_div,
            self.btn_mod, self.btn_pow, self.btn_fact,
            self.btn_exp, self.btn_cos, self.btn_sin, self.btn_atan, self.btn_pi
        ]
        col = 0
        row = 0
        for b in buttons:
            b.grid(row=row, column=col, padx=4, pady=4)
            col += 1
            if col > 5:
                col = 0
                row += 1

        self.result_var = tk.StringVar(value="Resultado: ")
        self.lbl_result = tk.Label(frm, textvariable=self.result_var, anchor="w")
        self.lbl_result.grid(row=3, column=0, columnspan=2, sticky="we", pady=8)

        actions = tk.Frame(frm)
        actions.grid(row=4, column=0, columnspan=2, pady=6)
        self.btn_clear = tk.Button(actions, text="Limpiar", width=10, command=self.clear)
        self.btn_exit = tk.Button(actions, text="Salir", width=10, command=self.destroy)
        self.btn_clear.grid(row=0, column=0, padx=6)
        self.btn_exit.grid(row=0, column=1, padx=6)

    # ---------- API ----------

    def set_controller(self, controller: object) -> None:
        self._controller = controller
        self.btn_add.config(command=self._controller.on_add)
        self.btn_sub.config(command=self._controller.on_sub)
        self.btn_mul.config(command=self._controller.on_mul)
        self.btn_div.config(command=self._controller.on_div)
        self.btn_mod.config(command=self._controller.on_mod)
        self.btn_pow.config(command=self._controller.on_pow)
        self.btn_fact.config(command=self._controller.on_factorial)
        self.btn_exp.config(command=self._controller.on_exp)
        self.btn_cos.config(command=self._controller.on_cos)
        self.btn_sin.config(command=self._controller.on_sin)
        self.btn_atan.config(command=self._controller.on_atan)
        self.btn_pi.config(command=self._controller.on_pi)

    def get_operands(self) -> Tuple[int, int]:
        a_text = self.entry_a.get().strip()
        b_text = self.entry_b.get().strip()
        if not a_text:
            raise ValueError("Ingrese un valor en Operando A.")
        if not b_text:
            raise ValueError("Ingrese un valor en Operando B.")
        return int(a_text), int(b_text)

    def get_single_operand(self) -> float:
        a_text = self.entry_a.get().strip()
        if not a_text:
            raise ValueError("Ingrese un valor en Operando A.")
        return float(a_text)

    def set_result(self, text: str) -> None:
        self.result_var.set(f"Resultado: {text}")

    def show_error(self, msg: str) -> None:
        messagebox.showerror("Error", msg)

    def clear(self) -> None:
        self.entry_a.delete(0, tk.END)
        self.entry_b.delete(0, tk.END)
        self.result_var.set("Resultado: ")
        self.entry_a.focus_set()
