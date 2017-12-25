from flask_restplus import fields

from viewer.api.restplus import api

namespace = api.model('Name space', {
    'name': fields.String(readOnly=True, description='name of a namespace'),
})

namespace_collection = api.model('List of namespaces available', {
    'items': fields.List(fields.Nested(namespace)),
})


kind = api.model('Kinds', {
    'name': fields.String(readOnly=True, description='Kind name'),
    'namespace': fields.String(readOnly=True, description='namespace of ')
})

kind_collection = api.model('List of kinds available', {
    'items': fields.List(fields.Nested(kind)),
})
