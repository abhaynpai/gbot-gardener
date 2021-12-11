from flask import Flask, Response, json, jsonify
from config.config import get_config
from time import sleep
import sys

import utils.garden as garden

app = Flask('__name__')

@app.route('/api/v1/tulsi/status', methods=['GET'])
def tulsi_status():
    data = {
        'moisture_status': garden.get_moisture_value()
    }
    return Response(json.dumps(data), mimetype='application/json')

@app.route('/api/v1/tulsi/water', methods=['POST'])
def water_plant():
    data = {
        'moisture': 234,
        'is_dry': True
    }
    return jsonify(data)

if __name__ == '__main__':
    counter = 0
    while counter < 10:
        print(f'moisture value reading is : {garden.get_moisture_value()}')
        sleep(1)
        counter += 1
        if counter == 10:
            garden.cleanup()
            sys.exit(0)
    conf = get_config()
    app.run(host=conf['host'], port=conf['port'], debug=True)
