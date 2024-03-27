from view.BaseTestTab import BaseTestTab


class VarianceTab(BaseTestTab):
    """
    Clase que representa la pestaña de la prueba de varianza en la interfaz gráfica.

    Hereda de BaseTestTab y se especializa para mostrar los resultados específicos de la prueba de varianza.
    """
    def __init__(self):
        """
        Inicializa una instancia de VarianceTab.

        Define los nombres de las pruebas y los resultados iniciales para la prueba de varianza.
        """
        test_names = ["𝑅", "𝜎^2", "1-(α/2)", "(α/2)", "𝑋(𝜎/2)^2", "𝑋 1-(𝜎/2)^2", "LI", "LS"]
        self.test_results = self.initialize_test_results(len(test_names))
        super().__init__(test_names, self.test_results)

    def set_test_results(self, test_results):
        """
        Establece los resultados de la prueba de varianza y actualiza la interfaz gráfica.

        Args:
            test_results (list): Lista de resultados de la prueba de varianza.
        """
        self.test_results = test_results
        super().set_test_results(test_results)
