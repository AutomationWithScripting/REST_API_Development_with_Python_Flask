from flask import Flask,jsonify,make_response,request
from flask_restful import Resource,Api

app=Flask(__name__)
api=Api(app)

employees_info = {
  "John": {
  "salary": "10L",
  "Technology": "Linux Admin"
  },
  "Kelly": {
  "salary": "1000$",
  "Technology": "Web Developer"
  }
}

class Help(Resource):
    def get(self):
        help={
          "All Endpoints": ["/esinfo"]
        }
        return help


class Employees(Resource):
    def get(self,ename=None):
        if request.args:
            if "ename" not in request.args.keys():
                message={
                "message": "Please use query paramter as ename only",
                "help": "/esinfo?ename=<your_emp_name>"
                }
                return make_response(jsonify(message),400)
            emp=request.args.get("ename")
            if emp in employees_info.keys():
                return make_response(jsonify(employees_info.get(emp)),200)
            else:
                message={
                "message": "Sorry!! We dont have this emp in our list"
                }
                return make_response(jsonify(message),404)
        else:
            return make_response(jsonify(employees_info),200)



api.add_resource(Help,"/")

api.add_resource( Employees, "/esinfo")

app.run(port=5000,host="localhost",debug=True)
