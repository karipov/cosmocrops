from flask import Flask, jsonify
from arduino import get_data
from datetime import datetime

app = Flask(__name__)

def round_to_two_decimals(number: float) -> float:
    return round(number, 2)

@app.route('/data')
def get_data():

    data = {
        'water_level': round(0.5 + (datetime.now().second / 60.0 / 4), 2),
        'humidity': round(0.6 - (datetime.now().second / 60.0 / 4), 2),
        'temperature': round(25.5 + (datetime.now().second), 2),
        'co2': 0.70,
        'light': 'on',
    }

    # fix when the arduino is connected
    # real_data = get_data()

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
