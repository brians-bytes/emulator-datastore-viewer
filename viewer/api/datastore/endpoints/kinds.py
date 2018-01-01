from flask_restplus import Resource

from viewer.api.datastore.serializers import kind_collection
from viewer.api.restplus import api
from viewer.models.kind import KindModel

ns = api.namespace('kinds', description='Kinds Endpoints')


@ns.route('')
class NamespaceCollection(Resource):
    @api.doc(params={
        'namespace': 'current namespace',
    })
    @api.marshal_with(kind_collection)
    def get(self):
        current_kinds = KindModel.get_available_namespaced_entity_kinds()
        return {
            'items': [
                {
                    'name': kind['kind'],
                    'namespace': kind['namespace'] or 'default',
                } for kind in current_kinds
            ],
        }
