from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    """ Say Hello world """
    def post(self):
        """ hello post method """
        data = request.get_json()
        return jsonify(data)

    def get(self):
        """hello from get method"""
        args = request.args
        return jsonify({ "message": {"hello": "world"}, "args": args, "Status Code": 200 } )

class GoodBye(Resource):
    """ Say goodbye """
    def post(self):
        """ hello post method """
        data = request.get_json()
        return jsonify(data)

    def get(self):
        """hello from get method"""
        args = request.args
        return jsonify({ "message": {"goodbye": "world"}, "args": args,  "Status Code": 200 } )


api.add_resource(Hello, '/hello')
api.add_resource(GoodBye, '/goodbye')

if __name__ == "__main__":
    app.run()