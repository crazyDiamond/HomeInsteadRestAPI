from flask import Flask
from flask import Response
import json

app = Flask(__name__)


@app.route('/caregivers', methods=['GET'])
def get_care_givers():
    care_givers = [
        {'id': 1, 'name':'Mary'}, 
        {'id': 2, 'name':'John'}
    ]
    jso = json.dumps(care_givers)

    resp = Response(jso, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()
