from flask import Flask, jsonify, request, redirect
from flask_restx import Resource, Api
from apis.todo import TodoSimple

app = Flask(__name__)
api = Api(app)

api.add_resource(TodoSimple, '/car')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')