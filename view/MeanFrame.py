from view.BaseTestTab import BaseTestTab


class MeanTab(BaseTestTab):
    """
    Clase que representa la pestaña de la prueba de media en la interfaz gráfica.

    Hereda de BaseTestTab y se especializa para mostrar los resultados específicos de la prueba de media.
    """
    def __init__(self):
        """
        Inicializa una instancia de MeanTab.

        Define los nombres de las pruebas y los resultados iniciales para la prueba de media.
        """
        test_names = ["α", "R", "1-(α/2)", "z", "LI", "LS"]
        self.test_results = self.initialize_test_results(len(test_names))
        super().__init__(test_names, self.test_results)

    def set_test_results(self, test_results):
        """
        Establece los resultados de la prueba de media y actualiza la interfaz gráfica.

        Args:
            test_results (list): Lista de resultados de la prueba de media.
        """
        self.test_results = test_results
        super().set_test_results(test_results)

