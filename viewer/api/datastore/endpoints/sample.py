from flask_restplus import Resource

from viewer.api.restplus import api

ns = api.namespace('sample', description='Sample endpoints')

@ns.route('')
class SampleResourceCollections(Resource):

    def get(self):
        pass
