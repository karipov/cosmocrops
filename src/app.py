from flask import Flask, jsonify
from arduino import get_data
from datetime import datetime

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {
        'water_level': 0.5 + (datetime.now().second / 60.0 / 4),
        'humidity': 0.6 - (datetime.now().second / 60.0 / 4),
        'temperature': 25.5 + (datetime.now().second),
        'co2': 0.7,
        'light': 'on',
    }

    # fix when the arduino is connected
    # real_data = get_data()

    response = jsonify(data)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
