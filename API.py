
# Crea una api sencilla

from flask import Flask, jsonify, request
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

class Hello(Resource):
    def get(self):
        return jsonify({'message': 'Hello world'})
    
    def post(self):
        some_json = request.get_json()
        return jsonify({'you sent': some_json}), 201
    
class Multi(Resource):
    def get(self, num):
        return jsonify({'result': num*10})
    
api.add_resource(Hello, '/')
api.add_resource(Multi, '/multi/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
