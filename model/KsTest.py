from model.Constants import Constants


class KsTest:
    """
    Clase para realizar la prueba de Kolmogorov-Smirnov en una lista de números pseudoaleatorios.

    Atributos:
        pseudo_random_numbers (list): Lista de números pseudoaleatorios a analizar.
        intervals_amount (int): Cantidad de intervalos en los que se divide el rango de los números pseudoaleatorios para la prueba.
        intervals (list): Lista de los límites superiores de cada intervalo.
        frequencies (list): Lista de frecuencias observadas de números pseudoaleatorios en cada intervalo.
        obtained_accumulated_frequency (list): Lista de frecuencias acumuladas observadas en cada intervalo.
        probability_obtained (list): Lista de probabilidades acumuladas observadas en cada intervalo.
        expected_accumulated_frequency (list): Lista de frecuencias acumuladas esperadas en cada intervalo bajo la hipótesis de uniformidad.
        probability_expected (list): Lista de probabilidades acumuladas esperadas en cada intervalo bajo la hipótesis de uniformidad.
        difference (list): Lista de diferencias absolutas entre las probabilidades acumuladas observadas y esperadas en cada intervalo.
        max_difference (float): Máxima diferencia absoluta entre las probabilidades acumuladas observadas y esperadas en todos los intervalos.
    """

    def __init__(self, intervals_amount):
        """
        Inicializa una instancia de la clase KsTest.

        Parámetros:
            intervals_amount (int): Cantidad de intervalos para la prueba de Kolmogorov-Smirnov.
        """
        self.pseudo_random_numbers = []
        self.intervals_amount = intervals_amount
        self.intervals = []
        self.frequencies = []
        self.obtained_accumulated_frequency = []
        self.probability_obtained = []
        self.expected_accumulated_frequency = []
        self.probability_expected = []
        self.difference = []
        self.max_difference = 0

    def execute_test(self):
        """
        Ejecuta la prueba de Kolmogorov-Smirnov y devuelve si los números pseudoaleatorios pasan la prueba.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario.
        """
        self.calculate_intervals()
        self.calculate_frequencies()
        self.calculate_obtained_frequencies()
        self.calculate_probabilities()
        self.calculate_expected_accumulated_frequencies()
        self.calculate_expected_probabilities()
        self.calculate_differences()
        return not (self.max_difference > Constants.DMAXP)

    def calculate_intervals(self):
        """
        Calcula los intervalos para la prueba de Kolmogorov-Smirnov.
        """
        start = 0
        end = 1
        width = (end - start) / self.intervals_amount
        aux = start
        for i in range(self.intervals_amount):
            aux += width
            self.intervals.append(round(aux, 2))

    def calculate_frequencies(self):
        """
        Calcula las frecuencias de los números pseudoaleatorios en cada intervalo.
        """
        self.frequencies = [0] * self.intervals_amount
        for number in self.pseudo_random_numbers:
            for i in range(len(self.intervals)):
                if number < self.intervals[i]:
                    self.frequencies[i] += 1
                    break

    def calculate_obtained_frequencies(self):
        """
        Calcula las frecuencias acumuladas obtenidas de los números pseudoaleatorios.
        """
        self.obtained_accumulated_frequency = [0] * self.intervals_amount
        for i in range(len(self.frequencies)):
            self.obtained_accumulated_frequency[i] = self.frequencies[i] + self.obtained_accumulated_frequency[i - 1]

    def calculate_probabilities(self):
        """
        Calcula las probabilidades acumuladas obtenidas de los números pseudoaleatorios.
        """
        self.probability_obtained = [0] * self.intervals_amount
        for i in range(len(self.obtained_accumulated_frequency)):
            self.probability_obtained[i] = self.obtained_accumulated_frequency[i] / len(self.pseudo_random_numbers)

    def calculate_expected_accumulated_frequencies(self):
        """
        Calcula las frecuencias acumuladas esperadas para cada intervalo.
        """
        self.expected_accumulated_frequency = [0] * self.intervals_amount
        expected_frequency = len(self.pseudo_random_numbers) / self.intervals_amount
        for i in range(len(self.probability_obtained)):
            self.expected_accumulated_frequency[i] = expected_frequency * (i + 1)

    def calculate_expected_probabilities(self):
        """
        Calcula las probabilidades acumuladas esperadas para cada intervalo.
        """
        self.probability_expected = [0] * self.intervals_amount
        for i in range(len(self.expected_accumulated_frequency)):
            self.probability_expected[i] = self.expected_accumulated_frequency[i] / len(self.pseudo_random_numbers)

    def calculate_differences(self):
        """
        Calcula las diferencias absolutas entre las probabilidades acumuladas obtenidas y esperadas.
        """
        self.difference = [0] * self.intervals_amount
        for i in range(len(self.difference)):
            self.difference[i] = round(abs(self.probability_expected[i] - self.probability_obtained[i]), 5)
        self.max_difference = max(self.difference)

    def set_pseudo_random_numbers(self, pseudo_random_numbers):
        """
        Establece la lista de números pseudoaleatorios para la prueba de Kolmogorov-Smirnov.

        Parámetros:
            pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        """
        self.pseudo_random_numbers = pseudo_random_numbers

    @property
    def get_max_difference(self):
        """
        Obtiene el valor de la Máxima diferencia entre las probabilidades acumuladas obtenidas y esperadas.

        Retorna:
            float: Valor Máxima diferencia.
        """
        return self.max_difference
