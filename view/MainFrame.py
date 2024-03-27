from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QTabWidget, QWidget, QVBoxLayout

from view.ChiFrame import ChiTab
from view.KsFrame import KsTab
from view.LoadFileFrame import LoadFileFrame
from view.MeanFrame import MeanTab
from view.PokerFrame import PokerTab
from view.VarianceFrame import VarianceTab


class MainFrame(QMainWindow):
    """
    Clase que representa la ventana principal de la aplicación.

    Contiene pestañas para cargar archivos, realizar pruebas estadísticas y mostrar los resultados.
    """
    def __init__(self):
        """
        Inicializa una instancia de MainFrame.
        """
        super().__init__()
        self.selected_file = None
        self.load_file_tab = LoadFileFrame()
        self.variance_tab = VarianceTab()
        self.mean_tab = MeanTab()
        self.ks_tab = KsTab()
        self.chi_tab = ChiTab()
        self.poker_tab = PokerTab()
        self.setup_ui()

    def setup_ui(self):
        """
        Configura la interfaz de usuario de la ventana principal.
        """

        # Establece el título de la ventana.
        self.setWindowTitle("Pseudo Number Tests")

        # Establece el tamaño de la ventana.
        self.resize(800, 600)

        # Crea un widget central y establece un layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Crea un QTabWidget para contener las pestañas
        tab_widget = QTabWidget()
        main_layout.addWidget(tab_widget)

        # Añade las pestañas al QTabWidget
        tab_widget.addTab(self.load_file_tab, "Load File")
        tab_widget.addTab(self.mean_tab, "Mean Test")
        tab_widget.addTab(self.variance_tab, "Variance Test")
        tab_widget.addTab(self.ks_tab, "KS Test")
        tab_widget.addTab(self.chi_tab, "Chi Test")
        tab_widget.addTab(self.poker_tab, "Poker Test")

    def display_result(self, tab_num, test_result):
        """
        Muestra el resultado de una prueba en la pestaña correspondiente.

        Args:
            tab_num (int): Número de la pestaña en la que se mostrará el resultado.
            test_result (str): Resultado de la prueba a mostrar.
        """
        if tab_num == 0:
            self.mean_tab.set_result_label(test_result)
        elif tab_num == 1:
            self.variance_tab.set_result_label(test_result)
        elif tab_num == 2:
            self.ks_tab.set_result_label(test_result)
        elif tab_num == 3:
            self.chi_tab.set_result_label(test_result)
        elif tab_num == 4:
            self.poker_tab.set_result_label(test_result)
        else:
            print("Pestaña no válida")

    def run_all_tests(self, test_functions):
        """
        Ejecuta todas las pruebas estadísticas y actualiza los resultados en la interfaz de usuario.

        Args:
            test_functions (list): Lista de funciones de prueba a ejecutar.
        """
        test_functions = test_functions
        for i, test_function in enumerate(test_functions):
            test_passed = test_function()
            status = "Passed" if test_passed else "Failed"
            self.load_file_tab.update_status(i, status)
