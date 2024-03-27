from collections import Counter

import numpy as np
from scipy.stats import chi2


class PokerTest:
    """
    Clase para realizar la prueba de póker en una lista de números pseudoaleatorios.

    Atributos:
        pseudo_random_numbers (list): Lista de números pseudoaleatorios a analizar.
        expected_counts (dict): Diccionario que contiene las frecuencias esperadas para cada categoría de mano de póker.
        category_counts (dict): Diccionario que contiene las frecuencias observadas para cada categoría de mano de póker.
        chi_squared (float): Valor de chi cuadrado calculado a partir de las frecuencias observadas y esperadas.
        x_square (float): Valor crítico de chi cuadrado para el nivel de significancia deseado.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase PokerTest.
        """
        self.pseudo_random_numbers = []
        self.expected_counts = {}
        self.category_counts = {}
        self.chi_squared = 0
        self.x_square = 0

    def classify_hand(self, digits):
        """
        Clasifica una mano de póker dada una secuencia de dígitos.

        Parámetros:
            digits (str): Secuencia de dígitos que representa una mano de póker.

        Retorna:
            str: Categoría de la mano de póker.
        """
        counts = Counter(digits).values()
        if len(counts) == 5:
            return 'Todos diferentes'
        elif len(counts) == 4:
            return 'Un par'
        elif len(counts) == 3:
            if 3 in counts:
                return 'Tercia'
            else:
                return 'Dos pares'
        elif len(counts) == 2:
            if 4 in counts:
                return 'Poker'
            else:
                return 'Full'
        else:
            return 'Quintillas'

    def execute_poker_test(self, digit_length=5):
        """
        Ejecuta la prueba de póker en la lista de números pseudoaleatorios.

        Parámetros:
            digit_length (int): Longitud de los dígitos a considerar para cada mano de póker.

        Retorna:
            bool: True si los números pseudoaleatorios pasan la prueba de póker, False de lo contrario.
        """

        # Genera la secuencia de manos a partir de los números pseudoaleatorios
        sequence = ''.join([str(number % 1)[2:7].ljust(5, '0') for number in self.pseudo_random_numbers])
        hands = [sequence[i:i + digit_length] for i in range(0, len(sequence), digit_length)]

        # Clasifica cada mano y cuenta la frecuencia de cada categoría
        categories = list(map(self.classify_hand, hands))
        self.category_counts = Counter(categories)

        # Asegúra que el valor de 'Quintillas' sea 0 si no está presente
        if 'Quintillas' not in self.category_counts:
            self.category_counts['Quintillas'] = 0

        # Calcula el número total de manos
        total_hands = len(hands)

        # Define las frecuencias esperadas para cada categoría de mano
        self.expected_counts = {
            'Todos diferentes': 0.3024 * total_hands,
            'Un par': 0.5040 * total_hands,
            'Dos pares': 0.1080 * total_hands,
            'Tercia': 0.0720 * total_hands,
            'Full': 0.0090 * total_hands,
            'Poker': 0.0045 * total_hands,
            'Quintillas': 0.0001 * total_hands
        }

        self.chi_squared = 0

        # Calcula la contribución de cada categoría al valor de chi cuadrado
        for category in self.expected_counts:
            observed = self.category_counts[category]
            expected = self.expected_counts[category]
            self.chi_squared += np.power((observed - expected), 2) / expected

        self.x_square = chi2.isf(0.05, 6)
        return self.chi_squared < self.x_square

    def set_pseudo_random_numbers(self, pseudo_random_numbers):
        """
        Establece la lista de números pseudoaleatorios para la prueba de póker.

        Parámetros:
            pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        """
        self.pseudo_random_numbers = pseudo_random_numbers
