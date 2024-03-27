from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
)
from PyQt6.QtGui import QPainter, QPolygonF
from PyQt6.QtCore import Qt, QPointF, pyqtSignal


class ChevronRightIcon(QWidget):
    """
    Clase que representa un icono de flecha hacia la derecha.

    Atributos heredados:
        parent (QWidget): Widget padre.
    """
    def __init__(self, parent=None):
        """
        Inicializa una instancia de ChevronRightIcon.

        Args:
            parent (QWidget, opcional): Widget padre. Por defecto es None.
        """
        super().__init__(parent)
        self.setMinimumSize(24, 24)

    def paintEvent(self, event):
        """
        Evento de pintado del widget. Dibuja el icono de flecha.

        Args:
            event (QPaintEvent): Evento de pintado.
        """
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.SolidLine)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        points = [
            QPointF(9, 18),
            QPointF(15, 12),
            QPointF(9, 6),
        ]
        polygon = QPolygonF(points)
        painter.drawPolyline(polygon)


class Card(QWidget):
    """
    Clase que representa una tarjeta con secciones para encabezado, contenido y pie de página.
    """
    def __init__(self):
        """
        Inicializa una instancia de Card.
        """
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.header = QWidget()
        self.header_layout = QHBoxLayout()
        self.header.setLayout(self.header_layout)
        self.layout.addWidget(self.header)

        self.content = QWidget()
        self.content_layout = QVBoxLayout()
        self.content.setLayout(self.content_layout)
        self.layout.addWidget(self.content)

        self.footer = QWidget()
        self.footer_layout = QHBoxLayout()
        self.footer.setLayout(self.footer_layout)
        self.layout.addWidget(self.footer)

    def add_header_widget(self, widget):
        """
        Agrega un widget al encabezado de la tarjeta.

        Args:
            widget (QWidget): Widget a agregar.
        """
        self.header_layout.addWidget(widget)

    def add_content_widget(self, widget):
        """
        Agrega un widget al contenido de la tarjeta.

        Args:
            widget (QWidget): Widget a agregar.
        """
        self.content_layout.addWidget(widget)

    def add_footer_widget(self, widget):
        """
        Agrega un widget al pie de página de la tarjeta.

        Args:
            widget (QWidget): Widget a agregar.
        """
        self.footer_layout.addWidget(widget)


class BaseTestTab(Card):
    """
    Clase base para pestañas que ejecutan y muestran resultados de pruebas estadísticas.

    Atributos:
        run_test_button_clicked (pyqtSignal): Señal emitida cuando se hace clic en el botón para ejecutar pruebas.
        result_label (str): Etiqueta para mostrar el resultado de la prueba.
    """
    run_test_button_clicked = pyqtSignal()
    result_label = ""

    def __init__(self, test_names, test_results):
        """
        Inicializa una instancia de BaseTestTab.

        Args:
            test_names (list): Lista de nombres de las pruebas.
            test_results (list): Lista de resultados de las pruebas.
        """
        super().__init__()
        self.test_names = test_names
        self.result_labels = []

        self.create_test_layout(test_results)

        self.run_tests_button = QPushButton("Run tests")
        self.run_tests_button.setStyleSheet("font-size: 12px;")
        self.run_tests_button.clicked.connect(self.run_test_button_clicked)
        self.add_footer_widget(self.run_tests_button)

    def create_test_layout(self, test_results):
        """
        Crea el layout para mostrar las pruebas y sus resultados.

        Args:
            test_results (list): Lista de resultados de las pruebas.
        """
        for test_name, test_result in zip(self.test_names, test_results):
            test_layout = QHBoxLayout()

            icon = ChevronRightIcon()
            icon.setMaximumSize(16, 16)  # Ajusta el tamaño si es necesario
            test_layout.addWidget(icon)

            test_label = QLabel(test_name)
            test_layout.addWidget(test_label, alignment=Qt.AlignmentFlag.AlignLeft)

            result_label = QLabel(str(test_result))  # Asegurarse de que sea una cadena
            self.result_labels.append(result_label)
            test_layout.addWidget(result_label, alignment=Qt.AlignmentFlag.AlignRight)

            test_layout.setSpacing(10)
            test_layout.setContentsMargins(0, 0, 0, 0)

            test_widget = QWidget()
            test_widget.setLayout(test_layout)
            self.add_content_widget(test_widget)

        test_result_label = QLabel("Test results: ")
        self.add_content_widget(test_result_label)

        self.result_label = QLabel()
        self.result_label.setStyleSheet("font-size: 12px;")
        self.add_content_widget(self.result_label)

    def set_result_label(self, result):
        """
        Establece el texto de la etiqueta del resultado de la prueba.

        Args:
            result (str): Resultado de la prueba.
        """
        self.result_label.setText(result)

    def set_test_results(self, test_results):
        """
        Establece los resultados de las pruebas.

        Args:
            test_results (list): Lista de resultados de las pruebas.
        """
        for label, result in zip(self.result_labels, test_results):
            label.setText(str(result))  # Actualizar el texto de la etiqueta

    def initialize_test_results(self, length, default_value="Pending"):
        """
        Inicializa los resultados de las pruebas con un valor predeterminado.

        Args:
            length (int): Cantidad de pruebas.
            default_value (str, opcional): Valor predeterminado para los resultados. Por defecto es "Pending".

        Returns:
            list: Lista de resultados de las pruebas inicializada.
        """
        return [default_value] * length
