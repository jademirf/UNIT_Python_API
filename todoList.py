from flask import Flask, request
from flask_restful import Resource,Api
import json

app = Flask(__name__)
api = Api(app)

tasks = []

class Task(Resource):
    def get(self):
        return tasks

    def post(self):
        newTask = json.loads(request.data)
        tasks.append(newTask)
        return {
            'message': 'Criado com sucesso!',
            'novaTask': newTask
        }

api.add_resource(Task, '/tasks/')

if __name__ == '__main__':
    app.run(debug=True)