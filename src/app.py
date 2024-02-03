from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data')
def get_data():
    data = {
        'water_level': 0.5,
        'humidity': 0.6,
        'temperature': 25.5,
        'co2': 0.7,
        'light': 'on',
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
