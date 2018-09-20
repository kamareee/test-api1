
import requests
from flask_restful import Api, Resource, reqparse


class HelloWorld(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('serviceID', type=str)
        json = parser.parse_args()
        service_id = json.get('serviceID')

        r = requests.get('http://localhost:5001/getParam', params=json)
        msg = r.json.get('Message')
        final_response = {'serviceID': str(service_id),
                          'message': str(msg)}

        return {"status": 'OK', "body": final_response}
