from flask_restplus import Resource

from viewer.api.datastore.serializers import kind_collection
from viewer.api.restplus import api

ns = api.namespace('properties', description='Properties Endpoints')


@ns.route('')
class PropertiesCollection(Resource):

    @api.doc(params={
        'namespace': 'current namespace',
    })
    @api.marshal_with(kind_collection)
    def get(self):
        return {
            'items': [
                {
                    'name': f'property {n_id}',
                    'namespace': 'default',
                }
                for n_id in range(10)
            ]
        }
