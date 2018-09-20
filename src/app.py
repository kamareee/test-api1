
from flask import Flask
from flask_restful import Api

from resources.entry_api import HelloWorld

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = 'mysecret'
api = Api(app)

api.add_resource(HelloWorld, '/expert.do')

if __name__ == '__main__':
    app.run(port=5000)
