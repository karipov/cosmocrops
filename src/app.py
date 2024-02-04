from flask import Flask, jsonify
from arduino import get_data_from_arduino
from datetime import datetime
from pins import output_fill, output_empty

app = Flask(__name__)

def round_to_two_decimals(number: float) -> float:
    return round(number, 2)

@app.route('/data')
def data():
    # data = {
    #     'water_level': round(0.5 + (datetime.now().second / 60.0 / 4), 2),
    #     'moisture': round(0.6 - (datetime.now().second / 60.0 / 4), 2),
    #     'temperature': round(25.5 + (datetime.now().second), 2),
    #     'light': 23,
    #     'timestamp': 1234567890,
    # }

    # fix when the arduino is connected
    raw_data = get_data_from_arduino()
    raw_data['timestamp'] = int(datetime.now().timestamp())

    # fix cors
    response = jsonify(raw_data)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/fill', methods=['POST'])
def fill():
    output_fill()
    return 'Filling'

@app.route('/empty', methods=['POST'])
def empty():
    output_empty()
    return 'Emptying'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
