from flask_restplus import Resource
from viewer.api.datastore.serializers import namespace_collection
from viewer.api.restplus import api
from viewer.models.name_space import NamespaceModel

ns = api.namespace('namespaces', description='Namespace Endpoints')


@ns.route('')
class NamespaceCollection(Resource):
    @api.marshal_with(namespace_collection)
    def get(self):
        available_namespaces = NamespaceModel.get_all_available_namespaces()
        return {
            'items': [{
                'name': namespace,
            } for namespace in available_namespaces]
        }
