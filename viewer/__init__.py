from flask import Flask, jsonify
from google.cloud import datastore
from oauth2client.client import GoogleCredentials

app = Flask(__name__)

from viewer.models.name_space import NamespaceModel
from viewer.models.kind import KindModel

credentials = GoogleCredentials.get_application_default()


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
