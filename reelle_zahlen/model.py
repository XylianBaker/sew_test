import requests
from abc import ABC, abstractmethod


class CalculationStrategy(ABC):
    """
    An abstract class representing a calculation strategy for finding the natural logarithm of a number.
    """

    def __init__(self):
        self.base_url = "http://127.0.0.1:5000/wurzel"

    @abstractmethod
    def get_natural_logarithm(self, number: float) -> str:
        """
        Calculate the natural logarithm of the given number.

        :param number: A float representing the number for which the natural logarithm should be calculated.
        :return: A string containing the formatted result of the natural logarithm calculation.
        """
        pass


class RealNumberStrategy(CalculationStrategy):
    """
    A concrete implementation of CalculationStrategy for real numbers.
    """

    def get_natural_logarithm(self, number: float) -> str:
        """
        Calculate the natural logarithm of the given real number.

        :param number: A float representing the real number for which the natural logarithm should be calculated.
        :return: A string containing the formatted result of the natural logarithm calculation.
        """
        params = {"zahl": str(number), "komplex": "false"}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 400:
            return f"Fehler: Der natürliche Logarithmus der Zahl <b>{number}</b> kann im reellen Zahlenraum <b>nicht " \
                   f"berechnet</b> werden"

        data = response.json()
        return f"Für die Zahl <b>{data['value']}</b> konnte der natürliche Logarithmus <b>{data['real']}</b> " \
               f"ermittelt werden"


class ComplexNumberStrategy(CalculationStrategy):
    """
    A concrete implementation of CalculationStrategy for complex numbers.
    """

    def get_natural_logarithm(self, number: float) -> str:
        """
        Calculate the natural logarithm of the given complex number.

        :param number: A float representing the complex number for which the natural logarithm should be calculated.
        :return: A string containing the formatted result of the natural logarithm calculation.
        """
        params = {"zahl": str(number), "komplex": "true"}
        response = requests.get(self.base_url, params=params)

        data = response.json()
        return f"Für die Zahl <b>{data['value']}</b> konnte der natürliche Logarithmus <b>({data['real']}+{data['imag']})</b> ermittelt werden"


def get_natural_logarithm(number: float, complex_numbers: bool) -> str:
    """
    Calculate the natural logarithm of the given number using the appropriate strategy based on the complex_numbers flag.

    :param number: A float representing the number for which the natural logarithm should be calculated.
    :param complex_numbers: A boolean indicating whether complex numbers should be considered (True) or not (False).
    :return: A string containing the formatted result of the natural logarithm calculation.
    """
    strategy = ComplexNumberStrategy() if complex_numbers else RealNumberStrategy()
    return strategy.get_natural_logarithm(number)


if __name__ == "__main__":
    print(get_natural_logarithm(2, False))
    print(get_natural_logarithm(2, True))
    print(get_natural_logarithm(0, False))
    print(get_natural_logarithm(4, False))
    print(get_natural_logarithm(4, True))
    print(get_natural_logarithm(-4, False))
    print(get_natural_logarithm(-4, True))
