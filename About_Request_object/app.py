from flask import Flask, make_response, jsonify, request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class Info(Resource):
    def __init__(self):
        #print(dir(request))
        #print(request.authorization)
        print(request.args)
    def get(self):
        print("get method is executed")
        pass
    def post(self):
        pass

api.add_resource(Info,"/info")
app.run(debug=True)
