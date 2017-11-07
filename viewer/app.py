from flask import Flask
from google.cloud import datastore

app = Flask(__name__)


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

    print('Saved {}: {}'.format(task.key.name, task['description']))
    return task


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
