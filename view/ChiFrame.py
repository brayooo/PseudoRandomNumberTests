from view.BaseTestTab import BaseTestTab


class ChiTab(BaseTestTab):
    """
    Clase que representa la pestaña de la prueba de Chi cuadrado en la interfaz gráfica.

    Hereda de BaseTestTab y se especializa para mostrar los resultados específicos de la prueba de Chi cuadrado.
    """
    def __init__(self):
        """
        Inicializa una instancia de MeanTab.

        Define los nombres de las pruebas y los resultados iniciales para la prueba de Chi cuadrado.
        """
        test_names = ["∑chi^2", "Chi inverso"]
        self.test_results = self.initialize_test_results(len(test_names))

        # Inicializa la pestaña con el título específico y los resultados de las pruebas.
        super().__init__(test_names, self.test_results)

    def set_test_results(self, test_results):
        """
        Establece los resultados de la prueba de Chi cuadrado y actualiza la interfaz gráfica.

        Args:
            test_results (list): Lista de resultados de la prueba de Chi cuadrado.
        """
        self.test_results = test_results
        super().set_test_results(test_results)
