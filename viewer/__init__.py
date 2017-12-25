from flask import Blueprint, Flask, jsonify
from google.cloud import datastore
from oauth2client.client import GoogleCredentials

from viewer.api.datastore.endpoints.kinds import ns as kind_ns
from viewer.api.datastore.endpoints.namespaces import ns as namespace_ns
from viewer.api.restplus import api
from viewer.models.kind import KindModel
from viewer.models.name_space import NamespaceModel

app = Flask(__name__)
credentials = GoogleCredentials.get_application_default()

blueprint = Blueprint('api', __name__, url_prefix='/api')
api.init_app(blueprint)
api.add_namespace(namespace_ns)
api.add_namespace(kind_ns)
app.register_blueprint(blueprint)


@app.route('/')
def hello_world():
    # Imports the Google Cloud client library
    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = 'Task'
    # The name/ID for the new entity
    name = 'sampletask1'
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task['description'] = 'Buy milk'

    # Saves the entity
    datastore_client.put(task)

    namespaces = NamespaceModel.get_all_available_namespaces()
    kinds = KindModel.get_all_available_kinds()
    return jsonify({
        'namespaces': namespaces,
        'kinds': kinds
    })
