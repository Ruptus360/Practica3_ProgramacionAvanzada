from typing import List


def leer_int(mensaje: str = "Introduce un número entero: ") -> int:
    """Lee un entero del teclado y lo pide de nuevo si no es válido."""
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: intente de nuevo")


def leer_float(mensaje: str = "Introduce un número decimal: ") -> float:
    """Lee un decimal del teclado y lo pide de nuevo si no es válido."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: pon coma flotante")


def crear_menu(opciones_menu: List[str]) -> int:
    """Muestra un menú y devuelve el número de la opción válida elegida."""
    for i, opcion in enumerate(opciones_menu):
        print(str(i + 1) + ". " + opcion)

    elegir = leer_int()

    if elegir <= 0 or elegir > len(opciones_menu):
        print("Error: fuera de rango")
        return crear_menu(opciones_menu)

    print("Opcion elegida: " + str(elegir))
    return elegir