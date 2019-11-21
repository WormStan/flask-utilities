from flask_restful import Resource, abort, fields, marshal_with, reqparse

from log import log

logger = log.setup_custom_logger('echarts_api')

echarts_data = {
    'pie': {
        'legend': ['passed', 'failed', 'blocked'],
        'data': [{'value': 35, 'name': 'passed'}, {'value': 60, 'name': 'failed'}, {'value': 70, 'name': 'blocked'}],
    },
    'line': {},
    'bar': {},
    'calendar': {}
}


def abort_if_type_doesnt_exist(type):
    if type not in echarts_data:
        abort(404, message=f"Chart Type {type} doesn't exist")

class EchartsApi(Resource):
    def __init__(self):
        pass

    def get(self, type):
        abort_if_type_doesnt_exist(type)
        return echarts_data[type]
