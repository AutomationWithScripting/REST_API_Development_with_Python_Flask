from flask import Flask
from flask_restful import Resource, Api

app=Flask(__name__)
api=Api(app)


employee_info = {
   "emp1": {
   "name": "xyz",
   "salary": "10L"
   },
   "emp2": {
   "name": "abc",
   "salary": "14L"
   }
}

class Employee(Resource):
    def get(self):
        return employee_info


api.add_resource(Employee,"/info")

app.run(port=5000,host="localhost")
