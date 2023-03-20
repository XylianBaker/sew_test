import requests
from abc import ABC, abstractmethod


class CalculationStrategy(ABC):
    def __init__(self):
        self.base_url = "http://127.0.0.1:5000/wurzel"

    @abstractmethod
    def get_natural_logarithm(self, number: float) -> str:
        pass


class RealNumberStrategy(CalculationStrategy):
    def get_natural_logarithm(self, number: float) -> str:
        params = {"zahl": str(number), "komplex": "false"}
        response = requests.get(self.base_url, params=params)

        if response.status_code == 400:
            return f"Fehler: Der natürliche Logarithmus der Zahl <b>{number}</b> kann im reellen Zahlenraum <b>nicht " \
                   f"berechnet</b> werden"

        data = response.json()
        return f"Für die Zahl <b>{data['value']}</b> konnte der natürliche Logarithmus <b>{data['real']}</b> " \
               f"ermittelt werden"


class ComplexNumberStrategy(CalculationStrategy):
    def get_natural_logarithm(self, number: float) -> str:
        params = {"zahl": str(number), "komplex": "true"}
        response = requests.get(self.base_url, params=params)

        data = response.json()
        return f"Für die Zahl <b>{data['value']}</b> konnte der natürliche Logarithmus <b>({data['real']}+{data['imag']})</b> ermittelt werden"


def get_natural_logarithm(number: float, complex_numbers: bool) -> str:
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
