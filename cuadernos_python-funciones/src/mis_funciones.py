"""Mis funciones personalizadas para el proyecto"""


def saludar(nombre):
    return f"Hola, {nombre}!"


def saludar_uno(nombre: str, saludo: str = "Hola") -> str:
    """Devuelve un saludo personalizado.

    Args:
        nombre: Nombre de la persona a saludar.
        saludo: Texto del saludo.
    """
    return f"{saludo}, {nombre}"
