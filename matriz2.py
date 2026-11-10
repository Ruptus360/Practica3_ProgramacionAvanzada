import numpy as np  # type: ignore

from utils import leer_int, leer_float, crear_menu


class MatrizFloat:
    """Clase que representa una matriz dinámica 1D/2D."""

    TIPO_DATO = np.float32

    def __init__(self) -> None:
        """Inicializa la matriz a None y las dimensiones a 0."""
        self._matriz: np.ndarray = None  # type: ignore
        self._nfil: int = 0
        self._ncol: int = 0

    @classmethod
    def matriz_identidad(cls, n: int) -> "MatrizFloat":
        """Crea y devuelve una nueva matriz identidad de tamaño n x n."""
        nueva = cls()
        nueva._matriz = np.eye(n, dtype=cls.TIPO_DATO)
        nueva._nfil = n
        nueva._ncol = n
        return nueva

    @staticmethod
    def mismas_dimensiones(m1: "MatrizFloat", m2: "MatrizFloat") -> bool:
        """Devuelve True si ambas matrices existen y tienen las mismas dimensiones."""
        if m1 is None or m2 is None or m1._matriz is None or m2._matriz is None:
            return False
        return m1._matriz.shape == m2._matriz.shape

    def crear_matriz2d(self, nfil: int, ncol: int) -> None:
        """Crea una matriz bidimensional de ceros de nfil x ncol."""
        self._matriz = np.zeros((nfil, ncol), dtype=self.TIPO_DATO)
        self._nfil = nfil
        self._ncol = ncol

    def crear_matriz1d(self, nelementos: int) -> None:
        """Crea una matriz unidimensional de ceros (1 fila y nelementos columnas)."""
        self.crear_matriz2d(1, nelementos)

    def existe(self) -> bool:
        """Devuelve True si la matriz está creada y no está vacía."""
        return self._matriz is not None and self._matriz.size > 0

    def introducir(self) -> None:
        """Pide por consola el valor de cada posición (i, j) de la matriz."""
        if not self.existe():
            print("Error: la matriz no esta creada")
            return
        for i in range(self._nfil):
            for j in range(self._ncol):
                mensaje = "Valor [" + str(i) + "][" + str(j) + "]: "
                self._matriz[i, j] = leer_float(mensaje)

    def mostrar(self) -> None:
        """Muestra las dimensiones y los elementos de la matriz."""
        if not self.existe():
            print("No existe tal cosa")
        else:
            print("Dimensiones: " + str(self._nfil) + " x " + str(self._ncol))
            print(self._matriz)

    def sumar_matrices(self, otra_matriz: "MatrizFloat") -> "MatrizFloat":
        """Devuelve una nueva matriz con la suma, o una matriz vacia si no coinciden."""
        if not self.mismas_dimensiones(self, otra_matriz):
            print("no coinciden dimensiones")
            return MatrizFloat()
        resultado = MatrizFloat()
        resultado._matriz = self._matriz + otra_matriz._matriz
        resultado._nfil = self._nfil
        resultado._ncol = self._ncol
        return resultado

    def restar_matrices(self, otra_matriz: "MatrizFloat") -> "MatrizFloat":
        """Devuelve una nueva matriz con la resta, o una matriz vacia si no coinciden."""
        if not self.mismas_dimensiones(self, otra_matriz):
            print("no coinciden dimensiones")
            return MatrizFloat()
        resultado = MatrizFloat()
        resultado._matriz = self._matriz - otra_matriz._matriz
        resultado._nfil = self._nfil
        resultado._ncol = self._ncol
        return resultado


def main() -> None:
    """Ejecuta el menú principal del programa."""
    opciones = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Construir matriz identidad",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Terminar",
    ]
    opciones_operaciones = [
        "Sumar matrices",
        "Restar matrices",
        "Volver al menu principal",
    ]

    matriz = MatrizFloat()

    while True:
        eleccion = crear_menu(opciones)

        if eleccion == 1:
            nelementos = leer_int("Numero de elementos: ")
            matriz.crear_matriz1d(nelementos)

        elif eleccion == 2:
            nfil = leer_int("Numero de filas: ")
            ncol = leer_int("Numero de columnas: ")
            matriz.crear_matriz2d(nfil, ncol)

        elif eleccion == 3:
            n = leer_int("Tamaño n: ")
            matriz = MatrizFloat.matriz_identidad(n)

        elif eleccion == 4:
            matriz.introducir()

        elif eleccion == 5:
            matriz.mostrar()

        elif eleccion == 6:
            operacion = crear_menu(opciones_operaciones)
            if operacion == 3:
                continue
            if not matriz.existe():
                print("Error: la matriz no esta creada")
                continue

            print("Segunda matriz")
            nfil = leer_int("Numero de filas: ")
            ncol = leer_int("Numero de columnas: ")
            otra_matriz = MatrizFloat()
            otra_matriz.crear_matriz2d(nfil, ncol)
            otra_matriz.introducir()

            if operacion == 1:
                resultado = matriz.sumar_matrices(otra_matriz)
            else:
                resultado = matriz.restar_matrices(otra_matriz)
            if resultado.existe():
                resultado.mostrar()

        elif eleccion == 7:
            print("Fin del programa")
            break


if __name__ == "__main__":
    main()