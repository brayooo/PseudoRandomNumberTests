from view.BaseTestTab import BaseTestTab


class PokerTab(BaseTestTab):
    """
    Clase que representa la pestaña de la prueba de Poker en la interfaz gráfica.

    Hereda de BaseTestTab y se especializa para mostrar los resultados específicos de la prueba de Poker.
    """
    def __init__(self):
        """
        Inicializa una instancia de PokerTab.

        Define los nombres de las pruebas y los resultados iniciales para la prueba de Poker.
        """
        test_names = ["Todos diferentes", "Un par", "Dos pares", "Tercia", "Full", "Poker", "Quintillas",
                      "Σ", "X^2"]
        self.test_results = self.initialize_test_results(len(test_names))
        super().__init__(test_names, self.test_results)

    def set_test_results(self, test_results):
        """
        Establece los resultados de la prueba de Poker y actualiza la interfaz gráfica.

        Args:
            test_results (list): Lista de resultados de la prueba de Poker.
        """
        self.test_results = test_results
        super().set_test_results(test_results)
