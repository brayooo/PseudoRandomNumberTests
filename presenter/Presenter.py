from model.Constants import Constants


class Presenter:
    """
    Esta clase se encarga de presentar los datos y resultados de las pruebas estadísticas al usuario.

    Atributos:
        model (Model): Instancia del modelo que contiene la lógica y los datos.
        view (View): Instancia de la vista que interactúa con el usuario.
    """
    def __init__(self, view, model) -> None:
        """
        Inicializa una instancia de la clase Presenter.

        Args:
            view (View): Instancia de la vista.
            model (Model): Instancia del modelo.
        """
        self.model = model
        self.view = view
        self.connect_signals()

    def set_data_to_model(self, data):
        """
        Establece los datos en el modelo.

        Args:
            data (list): Lista de números pseudoaleatorios.
        """
        self.model.set_pseudo_random_numbers(data)

    def presenter_mean_test(self):
        """
        Ejecuta y presenta los resultados de la prueba de media.
        """
        try:
            test_passed = self.model.execute_mean_test()
            status = "Passed" if test_passed else "Failed"
            self.view.display_result(0, status)
            data = [str(Constants.ALPHA), str(self.model.mean_test.r), str(self.model.mean_test.half_alpha),
                    str(self.model.mean_test.zeta), str(self.model.mean_test.lower_limit),
                    str(self.model.mean_test.higher_limit)]
            self.view.mean_tab.set_test_results(data)
        except Exception as e:
            print(f"Error al ejecutar la prueba de media: {e}")

    def presenter_variance_test(self):
        """
        Ejecuta y presenta los resultados de la prueba de varianza.
        """
        try:
            test_passed = self.model.execute_variance_test()
            status = "Passed" if test_passed else "Failed"
            self.view.display_result(1, status)
            data = [str(self.model.variance_test.mean), str(self.model.variance_test.variance),
                    str(self.model.variance_test.one_half_alpha), str(self.model.variance_test.half_alpha),
                    str(self.model.variance_test.complete_chi_invert), str(self.model.variance_test.half_chi_invert),
                    str(self.model.variance_test.lower_limit), str(self.model.variance_test.upper_limit)]
            self.view.variance_tab.set_test_results(data)
        except Exception as e:
            print(f"Error al ejecutar la prueba de varianza: {e}")

    def presenter_ks_test(self):
        """
        Ejecuta y presenta los resultados de la prueba de Kolmogorov-Smirnov.
        """
        try:
            test_passed = self.model.execute_ks_test()
            status = "Passed" if test_passed else "Failed"
            self.view.display_result(2, status)
            data = [str(self.model.ks_test.max_difference), str(Constants.DMAXP)]
            self.view.ks_tab.set_test_results(data)
        except Exception as e:
            print(f"Error al ejecutar la prueba de ks: {e}")

    def presenter_chi_test(self):
        """
        Ejecuta y presenta los resultados de la prueba de Chi-cuadrado.
        """
        try:
            test_passed = self.model.execute_chi_test()
            status = "Passed" if test_passed else "Failed"
            self.view.display_result(3, status)
            data = [str(self.model.chi_test.total_error), str(self.model.chi_test.chi_invert)]
            self.view.chi_tab.set_test_results(data)
        except Exception as e:
            print(f"Error al ejecutar la prueba de chi: {e}")

    def presenter_poker_test(self):
        """
        Ejecuta y presenta los resultados de la prueba de Poker.
        """
        test_passed = self.model.execute_poker_test()
        status = "Passed" if test_passed else "Failed"
        self.view.display_result(4, status)
        data = list(self.model.poker_test.category_counts.values())
        data.append(self.model.poker_test.chi_squared)
        data.append(self.model.poker_test.x_square)
        self.view.poker_tab.set_test_results(data)

    def run_all_test(self):
        """
        Ejecuta todas las pruebas estadísticas y presenta sus resultados.
        """
        test_functions = [self.model.execute_mean_test, self.model.execute_variance_test, self.model.execute_ks_test,
                          self.model.execute_chi_test, self.model.execute_poker_test]
        self.view.run_all_tests(test_functions)

    def connect_signals(self):
        """
        Conecta las señales entre la vista y el presentador.
        """
        self.view.mean_tab.run_tests_button.clicked.connect(self.presenter_mean_test)
        self.view.variance_tab.run_tests_button.clicked.connect(self.presenter_variance_test)
        self.view.ks_tab.run_tests_button.clicked.connect(self.presenter_ks_test)
        self.view.chi_tab.run_tests_button.clicked.connect(self.presenter_chi_test)
        self.view.poker_tab.run_tests_button.clicked.connect(self.presenter_poker_test)
        self.view.load_file_tab.load_file_signal.connect(self.set_data_to_model)
        self.view.load_file_tab.run_all_tests_button.clicked.connect(self.run_all_test)

    def run(self):
        """
        Muestra la vista principal de la aplicación.
        """
        self.view.show()
