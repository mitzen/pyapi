from flask import request, jsonify, redirect
from flask_restx import Resource
from models.employee import Employee
from flask_restx import reqparse
from utils.serializer import Serializer

todos = {}
model = Employee()

class TodoSimple(Resource):

    def get(self, ):
        d = Serializer.json_to_object(request.data, Employee)
        return jsonify("ok")

    def put(self, todo_id: Employee):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

    def post(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}
