from PyQt6.QtWidgets import QApplication

import view
import model


class Controller:
    """
    A controller class for managing the interaction between the view and the model.
    """

    def __init__(self):
        """
        Initialize the Controller by creating a view instance and displaying it.
        """
        self.view = view.View(self)
        self.view.show()

    def submit(self) -> None:
        """
        Calculate the natural logarithm based on user input and display the result in the view.
        """
        number = self.view.get_number()
        complex_numbers = self.view.get_checkbox()
        logarithm = model.get_natural_logarithm(number, complex_numbers)
        self.view.set_text_output(logarithm)
        if number >= 0  or complex_numbers:
            self.view.set_text_statusbar("Die Berechnung war ok")
        else:
            self.view.set_text_statusbar("Die Berechnung war leider nicht möglich!")

    def reset(self) -> None:
        """
        Reset the view to its initial state.
        """
        self.view.reset()


if __name__ == '__main__':
    app = QApplication([])
    controller = Controller()
    app.exec()
