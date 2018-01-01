from flask_restplus import Api

api = Api(version='0.1', title='Datastore API', description='DATASTORE viewer API')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    return {'message': message}, 500
