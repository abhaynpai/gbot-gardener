from flask import Flask, Response, json, jsonify
from config.config import get_config

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
    conf = get_config()
    app.run(host=conf['host'], port=conf['port'], debug=True)
