from flask_restplus import Resource

from viewer.api.datastore.serializers import kind_collection
from viewer.api.restplus import api

ns = api.namespace('kinds', description='Kinds Endpoints')


@ns.route('')
class NamespaceCollection(Resource):

    @api.marshal_with(kind_collection)
    def get(self):
        return {
            'items': [
                {
                    'name': f'kinds {n_id}',
                    'namespace': 'default',
                }
                for n_id in range(10)
            ]
        }
