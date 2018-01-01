from flask_restplus import Resource, reqparse
from viewer.api.datastore.serializers import kind_collection
from viewer.api.restplus import api
from viewer.models.kind import KindModel

ns = api.namespace('kinds', description='Kinds Endpoints')

parser = reqparse.RequestParser()
parser.add_argument('namespace', type=str, help='limit the search to this namespace')


@ns.route('')
class NamespaceCollection(Resource):
    @api.doc(params={
        'namespace': 'current namespace',
    })
    @api.marshal_with(kind_collection)
    def get(self):
        args = parser.parse_args()
        namespace = args['namespace']

        available_kinds = KindModel.get_available_namespaced_entity_kinds(namespace)
        return {
            'items': [{
                'name': kind['kind'],
                'namespace': kind['namespace'] or 'default',
            } for kind in available_kinds],
        }
