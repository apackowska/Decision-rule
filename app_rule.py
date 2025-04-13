from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    # Pobieranie danych wejściowych z parametrów query string
    data = request.args
    
    # Pobieranie wartości dla num1 i num2, jeśli nie podano, ustawiamy na 0
    try:
        num1 = float(data.get('num1', 0))
    except ValueError:
        num1 = 0
    try:
        num2 = float(data.get('num2', 0))
    except ValueError:
        num2 = 0

    # Obliczanie sumy i zastosowanie reguły decyzyjnej
    suma = num1 + num2
    prediction = 1 if suma > 5.8 else 0

    # Przygotowanie słownika z dodatkowymi informacjami zwrotnymi
    features_info = {
        "num1": num1,
        "num2": num2,
        "sum": suma,
        "rule": "Jeśli suma num1 + num2 > 5.8, to prediction = 1, w przeciwnym razie prediction = 0"
    }

    # Zwracanie odpowiedzi w formacie JSON
    return jsonify({
        "prediction": prediction,
        "features": features_info
    })

if __name__ == '__main__':
    app.run(debug=True)
