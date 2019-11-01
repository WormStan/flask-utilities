from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from restful_api_collection.database_api import DataBaseApi

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(DataBaseApi, '/DataBaseApi')

@app.route('/')
def index():
    return "Test Failed"

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5001)
