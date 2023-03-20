from flask import Flask, request, Response

import math
import cmath

app = Flask(__name__)

ZAHL = 4
KOMPLEX = False


# show usage
@app.route('/')
def index():
    return 'Usage: http://localhost:5000/wurzel[?zahl=wert[&komplex=true/false]]'


# help
@app.route('/help')
def hello():
    return 'Example: http://localhost:5000/wurzel?zahl=wert&komplex=true'


@app.route('/wurzel', methods=["GET", "POST"])
def my_calculation():
    """Liefert die Wurzel einer reellen Zahl

    .. :quickref: Wurzelberechnung einer reellen Zahl.

    **Beispiel für die korrekte Berechnung im reellen Zahlenraum**:

    .. sourcecode:: http

      GET /wurzel?zahl=4&komplex=false HTTP/1.1
      Host: localhost:5000
      Accept: text/html; charset=iso-8859-1

      HTTP/1.1 200 OK
      Content-Type: application/json

        {
          "value": 4.00,
          "real": 2.00,
        }


    **Beispiel für die korrekte Berechnung im komplexen Zahlenraum**:

    .. sourcecode:: http

      GET /wurzel?zahl=-9&komplex=true HTTP/1.1
      Host: localhost:5000
      Accept: text/html; charset=iso-8859-1

      HTTP/1.1 200 OK
      Content-Type: application/json

        {
          "value": -9.00,
          "real": 0.00,
          "imag": 3.00
        }


    **Beispiel für die fehlerhafte Berechnung im reellen Zahlenraum**:

    .. sourcecode:: http

      GET /wurzel?zahl=-9 HTTP/1.1
      Host: localhost:5000
      Accept: text/html; charset=iso-8859-1

      HTTP/1.1 400 OK
      Content-Type: application/json
    """
    zahl = int(request.args.get('zahl', default=ZAHL, type=float))
    komplex = request.args.get('komplex', default=KOMPLEX)

    if str(komplex).lower() in ['0', 'false', 'f']:
        komplex = False
    else:
        komplex = True

    if komplex is False:
        if zahl < 0:
            return Response(status=400)
        else:
            result = math.sqrt(zahl)
            return {"value": zahl, "real": result}
    else:
        result = cmath.sqrt(zahl)
        return {"value": zahl, "real": result.real, "imag": result.imag}


if __name__ == '__main__':
    print("Welcome to our Square Root Service!")
    app.run(debug=False)
