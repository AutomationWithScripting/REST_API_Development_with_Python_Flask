from flask import Flask, make_response,jsonify
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
        if ename:
            if ename in employees_info.keys():
                return make_response(jsonify(employees_info.get(ename)),200)
            else:
                message={ "message": "Sorry your employee is not found in my list" }
                return make_response(jsonify(message),404)
        else:
            return make_response(jsonify(employees_info),200)



api.add_resource(Help,"/")

api.add_resource( Employees, "/api/v1/esinfo","/api/v1/esinfo/<string:ename>")

app.run(debug=True,port=5000,host="localhost")
