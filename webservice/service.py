from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from restful_api_collection.database_api import DataBaseApi
from restful_api_collection.echarts_api import EchartsApi

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(DataBaseApi, '/DataBaseApi')
api.add_resource(EchartsApi,'/EchartsApi/<string:type>')

@app.route('/')
def index():
    return "Test Success"

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5001)
