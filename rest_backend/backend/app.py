# The logic that sets up the app.

from flask import Flask
from flask_restplus import Resource, Api

app = Flask(__name__)           # create a Flask WSGI application
api = Api(app)                  # Create a Flask-RESTPlus API

@api.route('/hello')            # Create a URL route ro this resource
class helloWorld(Resource):     # Create a RESTful resource
    def get(self):              # Create GET endpoint
        return {'hello': 'world'}

if __name__ == `__main__`:
    app.run(debug=True)