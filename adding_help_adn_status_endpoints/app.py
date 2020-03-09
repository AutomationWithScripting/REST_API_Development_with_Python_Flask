from flask import Flask, jsonify
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

class Help(Resource):
    def get(self):
        help={
        "Available REST APIs are": ["/ping","/info"]
        }
        return help

class Ping(Resource):
    def get(self):
        status={
        "status": "Alive"
        }
        return status


class Employee(Resource):
    def get(self):
        employee_info={
        "emp1": {
        "name": "xyz",
        "salary": "10L"
        },
        "emp2": {
        "name": "mnq",
        "salary": "20L"
        }
        }
        return jsonify(employee_info)


api.add_resource( Help ,"/" )
api.add_resource( Ping ,"/ping" )
api.add_resource( Employee, "/info")

app.run(port=5000,host='localhost')
