from scipy.stats import chi2

from model.Constants import Constants


class ChiTest:
    """
    Clase para realizar la prueba de Kolmogorov-Smirnov en una lista de números pseudoaleatorios.

    Atributos:
        pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        intervals_amount (int): Cantidad de intervalos para la prueba de Kolmogorov-Smirnov.
        intervals (list): Lista de los límites superiores de los intervalos.
        frequencies (list): Lista de frecuencias de números pseudoaleatorios en cada intervalo.
        obtained_accumulated_frequency (list): Lista de frecuencias acumuladas obtenidas.
        probability_obtained (list): Lista de probabilidades acumuladas obtenidas.
        expected_accumulated_frequency (list): Lista de frecuencias acumuladas esperadas.
        probability_expected (list): Lista de probabilidades acumuladas esperadas.
        difference (list): Lista de diferencias absolutas entre las probabilidades acumuladas obtenidas y esperadas.
        max_difference (float): Máxima diferencia entre las probabilidades acumuladas obtenidas y esperadas.
    """
    def __init__(self, intervals_amount):
        """
        Inicializa una instancia de la clase ChiTest.

        Parámetros:
            intervals_amount (int): Cantidad de intervalos para la prueba de chi-cuadrado.
        """
        self.pseudo_random_numbers = []
        self.intervals_amount = intervals_amount
        self.intervals = []
        self.frequencies = [0] * intervals_amount
        self.errors = [0] * self.intervals_amount
        self.total_error = 0
        self.chi_invert = 0

    def execute_chi_test(self):
        """
        Ejecuta la prueba de chi-cuadrado y devuelve si los números pseudoaleatorios pasan la prueba.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario.
        """
        self.calculate_intervals()
        self.calculate_frequencies()
        self.calculate_chi()
        self.chi_invert_test()
        return self.total_error < self.chi_invert

    def calculate_intervals(self):
        """
        Calcula los intervalos para la prueba de chi-cuadrado.
        """
        min_value = min(self.pseudo_random_numbers)
        max_value = max(self.pseudo_random_numbers)
        interval_width = (max_value - min_value) / self.intervals_amount
        self.intervals = [(min_value + interval_width) + interval_width * i for i in range(self.intervals_amount)]

    def calculate_frequencies(self):
        """
        Calcula las frecuencias de los números pseudoaleatorios en cada intervalo.
        """
        if not self.pseudo_random_numbers:
            raise ValueError("ni_values is empty")

        # Reinicia las frecuencias a cero
        self.frequencies = [0] * self.intervals_amount

        min_value = min(self.pseudo_random_numbers)
        interval_size = self.intervals[1] - self.intervals[0] if len(self.intervals) > 1 else 1

        for number in self.pseudo_random_numbers:
            interval_index = min(int((number - min_value) // interval_size), self.intervals_amount - 1)
            self.frequencies[interval_index] += 1

    def calculate_chi(self):
        """
        Calcula el valor chi-cuadrado total a partir de las frecuencias observadas y esperadas.
        """
        self.calculate_error()
        self.total_error = sum(self.errors)

    def calculate_error(self):
        """
        Calcula el error cuadrado para cada intervalo y lo almacena en la lista de errores.
        """
        expected_freq = len(self.pseudo_random_numbers) / self.intervals_amount
        for i in range(len(self.errors)):
            self.errors[i] = (self.frequencies[i] - expected_freq) ** 2 / expected_freq

    def chi_invert_test(self):
        """
        Calcula el valor crítico de chi-cuadrado invertido con un nivel de significancia alpha.
        """
        self.chi_invert = chi2.isf(Constants.ALPHA, len(self.intervals) - 1)

    def set_pseudo_random_numbers(self, pseudo_random_numbers):
        """
        Establece la lista de números pseudoaleatorios para la prueba de chi-cuadrado.

        Parámetros:
            pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        """
        self.pseudo_random_numbers = pseudo_random_numbers

    @property
    def get_total_error(self):
        """
        Obtiene el valor total del error chi-cuadrado calculado.

        Retorna:
            float: Valor total del error chi-cuadrado.
        """
        return self.total_error

    @property
    def get_chi_invert(self):
        """
        Obtiene el valor crítico de chi-cuadrado invertido calculado.

        Retorna:
            float: Valor crítico de chi-cuadrado invertido.
        """
        return self.chi_invert
