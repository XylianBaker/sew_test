from PyQt6.QtWidgets import *
from PyQt6 import uic


class View(QMainWindow):
    input: QDoubleSpinBox
    output: QTextBrowser
    complex_numbers: QCheckBox

    def __init__(self):
        super().__init__()
        uic.loadUi("./ui.ui", self)
        self.output.setReadOnly(True)

    def reset(self) -> None:
        self.input.setValue(0)
        self.output.clear()
        self.complex_numbers.setChecked(False)

    def set_text_statusbar(self, text: str) -> None:
        self.statusbar.showMessage(text)

    def get_text_input(self) -> float:
        return self.input.value()

    def set_text_output(self, text: str) -> None:
        self.output.setText(text)


if __name__ == '__main__':
    app = QApplication([])
    view = View()
    view.show()
    app.exec()
