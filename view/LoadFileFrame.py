from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QFileDialog, QTableWidget, QTableWidgetItem, QHBoxLayout, \
    QSpacerItem, QSizePolicy


def load_data(file_path):
    """
    Carga datos desde un archivo JSON.

    Args:
        file_path (str): Ruta del archivo JSON.

    Returns:
        list: Lista de números cargados del archivo.

    Raises:
        ValueError: Si el formato del archivo no es compatible.
    """
    import json
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data['numbers']
    else:
        raise ValueError("Unsupported file format")


class LoadFileFrame(QWidget):
    """
    Widget para cargar archivos y visualizar el estado de las pruebas.

    Atributos:
        load_file_signal (pyqtSignal): Señal emitida cuando se carga un archivo con éxito.
        run_tests_signal (pyqtSignal): Señal emitida para ejecutar todas las pruebas.
    """
    load_file_signal = pyqtSignal(list)
    run_tests_signal = pyqtSignal()

    def __init__(self):
        """
        Inicializa una instancia de LoadFileFrame.
        """
        super().__init__()
        self.run_all_tests_button = None
        self.tests_status_table = None
        self.file_data_table = None
        self.load_file_button = None
        self.file_data = None
        self.create_load_file_tab()

    def create_load_file_tab(self):
        """
        Crea la interfaz gráfica para cargar archivos y visualizar el estado de las pruebas.
        """
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.file_data_table = QTableWidget()
        layout.addWidget(self.file_data_table)

        button_layout = QHBoxLayout()

        self.load_file_button = QPushButton("Load Files")
        self.load_file_button.clicked.connect(self.load_file)
        button_layout.addWidget(self.load_file_button)

        self.run_all_tests_button = QPushButton("Run All Tests")
        self.run_all_tests_button.clicked.connect(self.run_tests_signal)
        button_layout.addWidget(self.run_all_tests_button)

        layout.addLayout(button_layout)

        self.tests_status_table = QTableWidget(5, 2)
        self.tests_status_table.setHorizontalHeaderLabels(["Test Name", "Status"])

        test_names = ["Mean Test", "Variance Test", "Ks Test", "Chi Test", "Poker Test"]
        for i, test_name in enumerate(test_names):
            self.tests_status_table.setItem(i, 0, QTableWidgetItem(test_name))
            self.tests_status_table.setItem(i, 1, QTableWidgetItem("Not Run"))

        # Deshabilita la edición y la selección para toda la tabla
        self.tests_status_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tests_status_table.setSelectionMode(QTableWidget.SelectionMode.NoSelection)

        tests_status_layout = QHBoxLayout()

        tests_status_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        tests_status_layout.addWidget(self.tests_status_table)
        tests_status_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        layout.addLayout(tests_status_layout)

    def load_file(self):
        """
        Abre un cuadro de diálogo para seleccionar y cargar un archivo, y actualiza la tabla de datos.
        """
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "JSON Files (*.json)")
        if file_name:
            try:
                self.file_data = load_data(file_name)
                self.update_file_data_table()
                self.load_file_signal.emit(self.file_data)
            except Exception as e:
                print(f"Error al cargar el archivo: {e}")

    def update_file_data_table(self):
        """
        Actualiza la tabla de datos con los números cargados del archivo.
        """
        try:
            self.file_data_table.clear()

            if not self.file_data:  # If there's no data, there's nothing to update
                return

            # Limit the number of data to display to 100
            display_data = self.file_data[:1000]

            # Assuming file_data is a list of numbers
            self.file_data_table.setColumnCount(len(display_data))  # One column for each number
            self.file_data_table.setHorizontalHeaderLabels([f"Number {i + 1}" for i in range(len(display_data))])
            self.file_data_table.setRowCount(1)  # Only one row

            for i, number in enumerate(display_data):
                self.file_data_table.setItem(0, i, QTableWidgetItem(
                    str(number)))  # Set the number in the first row and i-th column
        except Exception as e:
            print(f"Error al actualizar la tabla de datos: {e}")

    def update_status(self, test_index, status):
        """
        Actualiza el estado de una prueba específica en la tabla de estado de las pruebas.

        Args:
            test_index (int): Índice de la prueba cuyo estado se va a actualizar.
            status (str): Nuevo estado de la prueba, por ejemplo "Passed" o "Failed".
        """
        self.tests_status_table.setItem(test_index, 1, QTableWidgetItem(status))