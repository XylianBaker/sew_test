from PyQt6.QtWidgets import *
from PyQt6 import uic
from controller import Controller


class View(QMainWindow):
    """
    A view class representing the graphical user interface of the application.
    """
    input: QDoubleSpinBox
    output: QTextBrowser
    checkbox_complex_numbers: QCheckBox

    def __init__(self, controller: Controller):
        """
        Initialize the View by loading the user interface and connecting the buttons to the controller.

        :param controller: The controller instance to handle user input.
        """
        super().__init__()
        uic.loadUi("./ui.ui", self)
        self.button_calculate.clicked.connect(controller.submit)
        self.button_reset.clicked.connect(controller.reset)
        self.output.setReadOnly(True)

    def reset(self) -> None:
        """
        Reset the user interface elements to their initial state.
        """
        self.input.setValue(0)
        self.output.clear()
        self.checkbox_complex_numbers.setChecked(False)
        self.set_text_statusbar("keine Berechnung durchgeführt")

    def set_text_statusbar(self, text: str) -> None:
        """
        Set the text of the status bar.

        :param text: The text to display in the status bar.
        """
        self.statusBar().showMessage(text)

    def get_number(self) -> float:
        """
        Get the number from the input field.

        :return: The number entered by the user as a float.
        """
        return self.input.value()

    def get_checkbox(self) -> bool:
        """
        Check if the complex numbers checkbox is checked.

        :return: True if the complex numbers checkbox is checked, False otherwise.
        """
        return self.checkbox_complex_numbers.isChecked()

    def set_text_output(self, text: str) -> None:
        """
        Set the text of the output field.

        :param text: The text to display in the output field.
        """
        self.output.setText(text)


if __name__ == '__main__':
    app = QApplication([])
    view = View(Controller())
    view.show()
    app.exec()
