from flask import Flask, jsonify,make_response,request
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
          "All Endpoints": ["/api/v1/esinfo","/api/v1/esinfo/:ename"]
        }
        return help


class Employees(Resource):
    def get(self,ename=None):
        print(request.args)
        if request.args:
            if "ename" not in request.args.keys():
                message={
                "message": "Please pass query paramter as ename only",
                "help": "/esinfo?ename=<your_emp_name>"
                }
                return make_response(jsonify(message),400)
            ename=request.args.get("ename")
            if ename in employees_info.keys():
                return employees_info.get(ename)
            else:
                message={
                "message": "Sorry your employee is not found in my list"
                }
                return make_response(jsonify(message),200)
        else:
            return make_response(jsonify(employees_info),200)



api.add_resource(Help,"/")

api.add_resource( Employees, "/api/v1/esinfo","/api/v1/esinfo/<string:ename>")

app.run(port=5000,host="localhost",debug=True)
