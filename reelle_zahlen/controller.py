from PyQt6.QtWidgets import QApplication

import view
import model


class Controller:
    def __init__(self):
        self.view = view.View(self)
        self.view.show()

    def submit(self) -> None:
        number = self.view.get_number()
        complex_numbers = self.view.get_checkbox()
        logarithm = model.get_natural_logarithm(number, complex_numbers)
        self.view.set_text_output(logarithm)
        if number >= 0  or complex_numbers:
            self.view.set_text_statusbar("Die Berechnung war ok")
        else:
            self.view.set_text_statusbar("Die Berechnung war leider nicht möglich!")

    def reset(self) -> None:
        self.view.reset()


if __name__ == '__main__':
    app = QApplication([])
    controller = Controller()
    app.exec()
