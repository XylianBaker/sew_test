from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):
    input: QDoubleSpinBox
    output: QTextBrowser
    checkbox_complex_numbers: QCheckBox

    def __init__(self, controller: Controller):
        super().__init__()
        uic.loadUi("./ui.ui", self)
        self.button_calculate.clicked.connect(controller.submit)
        self.button_reset.clicked.connect(controller.reset)
        self.output.setReadOnly(True)

    def reset(self) -> None:
        self.input.setValue(0)
        self.output.clear()
        self.checkbox_complex_numbers.setChecked(False)
        self.set_text_statusbar("keine Berechnung durchgeführt")

    def set_text_statusbar(self, text: str) -> None:
        self.statusBar().showMessage(text)

    def get_number(self) -> float:
        return self.input.value()

    def get_checkbox(self) -> bool:
        return self.checkbox_complex_numbers.isChecked()

    def set_text_output(self, text: str) -> None:
        self.output.setText(text)


if __name__ == '__main__':
    app = QApplication([])
    view = View(Controller())
    view.show()
    app.exec()
