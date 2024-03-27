import sys
from PyQt6.QtWidgets import QApplication

from model.Tests import Tests
from presenter.Presenter import Presenter
from view.MainFrame import MainFrame


def main():
    app = QApplication(sys.argv)
    view = MainFrame()
    model = Tests()
    presenter = Presenter(view, model)
    presenter.run()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
