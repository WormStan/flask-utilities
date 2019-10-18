from flask_restful import Resource, fields, marshal_with, reqparse

from log import log
from models_controller.common_controller import Common_Controller

logger = log.setup_custom_logger('database_api')

resource_fields = {
    'string_col': fields.String,
    'bool_col': fields.Boolean,
    'content_col': fields.String,
    'datetime_col': fields.String
}


class DataBaseApi(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.cc = Common_Controller()

    @marshal_with(resource_fields)
    def get(self):
        get_result = self.cc.bs_get_all()
        return get_result

    def post(self):

        self.parser.add_argument('input_par_1', type=str)
        self.parser.add_argument('input_par_2', type=str)

        args = self.parser.parse_args()

        input_par_1 = args['input_par_1']
        input_par_2 = args['input_par_2']

        return {
            'input_par_1': input_par_1,
            'input_par_2': input_par_2
        }
