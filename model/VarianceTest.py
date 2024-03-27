import numpy as np
from scipy.stats import chi2
from model.Constants import Constants
from statistics import mean

from model.util.MathUtils import MathUtils


class VarianceTest:
    """
    Esta clase se encarga de realizar la prueba de varianza para una lista de números pseudoaleatorios.

    Atributos:
        pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        mean (float): Media de los números pseudoaleatorios.
        one_half_alpha (float): Valor de (1 - alpha/2).
        half_alpha (float): Valor de (alpha/2).
        complete_chi_invert (float): Valor inverso de la distribución chi-cuadrado para (1 - alpha/2).
        half_chi_invert (float): Valor inverso de la distribución chi-cuadrado para (alpha/2).
        lower_limit (float): Límite inferior del intervalo de confianza.
        upper_limit (float): Límite superior del intervalo de confianza.
        variance (float): Varianza de los números pseudoaleatorios.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase VarianceTest.
        """
        self.pseudo_random_numbers = []
        self.mean = None
        self.one_half_alpha = None
        self.half_alpha = None
        self.complete_chi_invert = None
        self.half_chi_invert = None
        self.lower_limit = None
        self.upper_limit = None
        self.variance = None

    def execute_test(self):
        """"
        Realiza la prueba de varianza.

        Calcula la varianza de los números pseudoaleatorios y verifica si esta se encuentra dentro del intervalo de confianza especificado.

        Retorna:
            bool: True si la varianza está dentro del intervalo de confianza, False en caso contrario.
        """
        n = len(self.pseudo_random_numbers) - 1
        self.mean = mean(self.pseudo_random_numbers)
        self.variance = MathUtils.truncate(self.calculate_variance())
        self.one_half_alpha = 1 - (Constants.ALPHA / 2)
        self.half_alpha = Constants.ALPHA / 2
        self.complete_chi_invert = MathUtils.truncate(chi2.ppf(self.one_half_alpha, n))
        self.half_chi_invert = MathUtils.truncate(chi2.ppf(self.half_alpha, n))
        self.lower_limit = MathUtils.truncate(self.complete_chi_invert / (12 * n))
        self.upper_limit = MathUtils.truncate(self.half_chi_invert / (12 * n))
        return self.upper_limit <= self.variance <= self.lower_limit

    def calculate_variance(self):
        """
        Calcula la varianza de los números pseudoaleatorios.

        Retorna:
            float: Varianza de los números pseudoaleatorios.
        """
        variance = np.var(self.pseudo_random_numbers)
        return variance

    def set_pseudo_random_numbers(self, flat_list):
        """
        Establece la lista de números pseudoaleatorios.

        Args:
            flat_list (list): Lista de números pseudoaleatorios.
        """
        self.pseudo_random_numbers = flat_list

    @property
    def get_mean(self):
        """Obtiene la media de los números pseudoaleatorios."""
        return self.mean

    @property
    def get_variance(self):
        """Obtiene la varianza de los números pseudoaleatorios."""
        return self.variance

    @property
    def get_one_half_alpha(self):
        """Obtiene el valor de (1 - alpha/2)."""
        return self.one_half_alpha

    @property
    def get_half_alpha(self):
        """Obtiene el valor de (alpha/2)."""
        return self.half_alpha

    @property
    def get_complete_chi_invert(self):
        """Obtiene el valor inverso de la distribución chi-cuadrado para (1 - alpha/2)."""
        return self.complete_chi_invert

    @property
    def get_half_chi_invert(self):
        """Obtiene el valor inverso de la distribución chi-cuadrado para (alpha/2)."""
        return self.half_chi_invert

    @property
    def get_lower_limit(self):
        """Obtiene el límite inferior del intervalo de confianza."""
        return self.lower_limit

    @property
    def get_upper_limit(self):
        """Obtiene el límite superior del intervalo de confianza."""
        return self.upper_limit

