from flask_restful import Resource

skills = [
    'Java',
    'Python',
    'Nodejs',
    'PHP',
    'Mongodb',
    'Lua',
    'Go'
]

class Skills(Resource):
    def get(self):
        return skills