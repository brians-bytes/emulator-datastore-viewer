from flask_restplus import Resource

from viewer.api.datastore.serializers import namespace_collection
from viewer.api.restplus import api

ns = api.namespace('namespaces', description='Namespace Endpoints')


@ns.route('')
class NamespaceCollection(Resource):

    @api.marshal_with(namespace_collection)
    def get(self):
        return {
            'items': [
                {'name': f'namespace {n_id}'}
                for n_id in range(10)
            ]
        }
