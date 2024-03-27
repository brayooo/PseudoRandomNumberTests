from model.ChiTest import ChiTest
from model.KsTest import KsTest
from model.MeanTest import MeanTest
from model.PokerTest import PokerTest
from model.VarianceTest import VarianceTest


class Tests:
    """
    Clase que agrupa y ejecuta diferentes pruebas estadísticas en una lista de números pseudoaleatorios.

    Atributos:
        mean_test (MeanTest): Instancia de la clase MeanTest para realizar la prueba de la media.
        variance_test (VarianceTest): Instancia de la clase VarianceTest para realizar la prueba de la varianza.
        ks_test (KsTest): Instancia de la clase KsTest para realizar la prueba de Kolmogorov-Smirnov.
        chi_test (ChiTest): Instancia de la clase ChiTest para realizar la prueba de chi cuadrado.
        poker_test (PokerTest): Instancia de la clase PokerTest para realizar la prueba de póker.
    """
    def __init__(self):
        """
        Inicializa una instancia de la clase Tests.
        """
        self.mean_test = MeanTest()
        self.variance_test = VarianceTest()
        self.ks_test = KsTest(10)
        self.chi_test = ChiTest(10)
        self.poker_test = PokerTest()

    def set_pseudo_random_numbers(self, pseudo_random_numbers):
        """
        Establece la lista de números pseudoaleatorios para todas las pruebas.

        Parámetros:
            pseudo_random_numbers (list): Lista de números pseudoaleatorios.
        """
        self.mean_test.set_pseudo_random_numbers(pseudo_random_numbers)
        self.variance_test.set_pseudo_random_numbers(pseudo_random_numbers)
        self.ks_test.set_pseudo_random_numbers(pseudo_random_numbers)
        self.chi_test.set_pseudo_random_numbers(pseudo_random_numbers)
        self.poker_test.set_pseudo_random_numbers(pseudo_random_numbers)

    def execute_mean_test(self):
        """
        Ejecuta la prueba de la media.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario, o None en caso de error.
        """
        try:
            return self.mean_test.execute_test()
        except Exception as e:
            print(f"Error al ejecutar la prueba de media: {e}")
            return None

    def execute_variance_test(self):
        """
        Ejecuta la prueba de la media.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario, o None en caso de error.
        """
        try:
            return self.variance_test.execute_test()
        except Exception as e:
            print(f"Error al ejecutar la prueba de varianza: {e}")
            return None

    def execute_ks_test(self):
        """
        Ejecuta la prueba de la Kolmogorov Kolmogorov-Smirnov.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario, o None en caso de error.
        """
        try:
            return self.ks_test.execute_test()
        except Exception as e:
            print(f"Error al ejecutar la prueba de Kolmogorov-Smirnov: {e}")
            return None

    def execute_chi_test(self):
        """
        Ejecuta la prueba chi cuadrado.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario, o None en caso de error.
        """
        try:
            return self.chi_test.execute_chi_test()
        except Exception as e:
            print(f"Error al ejecutar la prueba de Chi Cuadrada: {e}")
            return None

    def execute_poker_test(self):
        """
        Ejecuta la prueba de poker.

        Retorna:
            bool: True si los números pasan la prueba, False de lo contrario, o None en caso de error.
        """
        try:
            return self.poker_test.execute_poker_test()
        except Exception as e:
            print(f"Error al ejecutar la prueba de Poker: {e}")
            return None
