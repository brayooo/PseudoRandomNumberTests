import math

from scipy.stats import norm
from model.Constants import Constants
from statistics import mean


class MeanTest:
    """
    Clase para realizar la prueba de la media en una lista de números pseudoaleatorios.

    Atributos:
        pseudo_random_numbers (list): Lista de números pseudoaleatorios a analizar.
        r (float): Promedio de los números pseudoaleatorios.
        half_alpha (float): Mitad del nivel de significancia alpha.
        zeta (float): Valor crítico de la distribución normal estándar para el nivel de confianza.
        lower_limit (float): Límite inferior del intervalo de confianza para la media.
        higher_limit (float): Límite superior del intervalo de confianza para la media.
        status (bool): Indica si los números pseudoaleatorios pasan la prueba de la media.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase MeanTest.
        """
        self.pseudo_random_numbers = []
        self.r = 0
        self.half_alpha = 0
        self.zeta = 0
        self.lower_limit = 0
        self.higher_limit = 0
        self.status = False

    def set_pseudo_random_numbers(self, pseudo_random_numbers):
        """
        Establece la lista de números pseudoaleatorios para la prueba de la media.

        Parámetros:
            pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        """
        self.pseudo_random_numbers = pseudo_random_numbers

    def calculate_average(self):
        """
        Calcula el promedio de la lista de números pseudoaleatorios.
        """
        if self.pseudo_random_numbers:
            self.r = mean(self.pseudo_random_numbers)
        return self.r

    def calculate_zeta(self):
        """
        Calcula el valor crítico de la distribución normal estándar para el nivel de confianza.
        """
        self.half_alpha = 1 - (Constants.ALPHA / 2)
        self.zeta = norm.ppf(self.half_alpha)

    def calculate_lower_limit(self, zeta, n):
        """
        Calcula el límite inferior del intervalo de confianza para la media.

        Parámetros:
            zeta (float): Valor crítico de la distribución normal estándar.
            n (int): Tamaño de la muestra (cantidad de números pseudoaleatorios).

        Retorna:
            float: Límite inferior del intervalo de confianza.
        """
        self.lower_limit = 0.5 - zeta * (1 / math.sqrt(12 * n)) if n > 0 else 0
        return self.lower_limit

    def calculate_higher_limit(self, zeta, n):
        """
        Calcula el límite superior del intervalo de confianza para la media.

        Parámetros:
            zeta (float): Valor crítico de la distribución normal estándar.
            n (int): Tamaño de la muestra (cantidad de números pseudoaleatorios).

        Retorna:
            float: Límite superior del intervalo de confianza.
        """
        self.higher_limit = 0.5 + zeta * (1 / math.sqrt(12 * n)) if n > 0 else 0
        return self.higher_limit

    def execute_test(self):
        """
        Ejecuta la prueba de la media y determina si los números pseudoaleatorios pasan la prueba.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario.
        """
        if not self.pseudo_random_numbers:
            print("La lista de números pseudoaleatorios está vacía.")
            return False
        self.calculate_average()
        self.calculate_zeta()
        n = len(self.pseudo_random_numbers)
        self.lower_limit = self.calculate_lower_limit(self.zeta, n)
        self.higher_limit = self.calculate_higher_limit(self.zeta, n)
        self.status = self.lower_limit <= self.r <= self.higher_limit
        return self.status

    @property
    def get_r(self):
        """
        Obtiene el promedio de los números pseudoaleatorios.

        Retorna:
            float: Promedio de los números pseudoaleatorios.
        """
        return self.r

    @property
    def get_half_alpha(self):
        """
        Obtiene la mitad del nivel de significancia alpha.

        Retorna:
            float: Mitad del nivel de significancia alpha.
        """
        return self.half_alpha

    @property
    def get_zeta(self):
        """
        Obtiene el valor crítico de la distribución normal estándar para el nivel de confianza.

        Retorna:
            float: Valor crítico de la distribución normal estándar.
        """
        return self.zeta

    @property
    def get_lower_limit(self):
        """
        Obtiene el límite inferior del intervalo de confianza para la media.

        Retorna:
            float: Límite inferior del intervalo de confianza.
        """
        return self.lower_limit

    @property
    def get_higher_limit(self):
        """
        Obtiene el límite superior del intervalo de confianza para la media.

        Retorna:
            float: Límite superior del intervalo de confianza.
        """
        return self.higher_limit
