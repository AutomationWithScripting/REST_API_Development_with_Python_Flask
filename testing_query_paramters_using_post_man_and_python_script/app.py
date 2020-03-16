from flask import Flask,request,jsonify,make_response
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
    def get(self):
        print(request.args)
        if request.args:
            if "ename" not in request.args.keys():
                message={
                "message": "Use only ename as query paramter",
                "help": "/esinfo?ename=<your_emp_name>"
                }
                return make_response(jsonify(message),200)
            emp_name=request.args.get("ename")
            if emp_name in employees_info.keys():
                return employees_info.get(emp_name)
            message={
            "message": "Sorry!!! We do not find given emp name in our list"
            }
            return make_response(jsonify(message),404)
        return make_response(jsonify(employees_info),200)



api.add_resource(Help,"/")

api.add_resource( Employees, "/esinfo")

app.run(port=5000,host="localhost",debug=True)
