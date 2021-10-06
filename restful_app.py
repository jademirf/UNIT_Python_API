from flask import Flask, request
from flask_restful import Resource, Api
from skills import Skills

import json

app = Flask(__name__)
api = Api(app)

developers = [
    {
        "name": "Desmennyellysson",
        "skills": [
            "Python",
            "Javascript"
        ]
    },
    {
        "name": "Jubscleiton",
        "skills": [
            "Java",
            "C#"
        ]
    }
]

class Devs(Resource):
    def get(self):
        return {'status': 200, 'data': developers}

    def post(self):
        newDev = json.loads(request.data)
        developers.append(newDev)
        return {
            "message": "Created!",
            "newValue": newDev
        }

class Dev(Resource):
    def get(self, indice):
        try:
            return developers[indice]
        except IndexError:
            mensagem = "O índice {} não foi encontrado no array".format(indice)
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }
        except:
            mensagem = "Erro desconhecido"
            return {
                "status": "Erro de índice",
                "message": mensagem,
            }

    def put(self, indice):
        # newValue recebe os dados do corpo da requisição e passa para o formato json
        newValue = json.loads(request.data)
        # Altera o valor da lista no indice informado com o novo valor recebido
        developers[indice] = newValue
        return {
            "message": "Updated!",
            "newValue": newValue
        }

    def delete(self, indice):
        developers.pop(indice)
        return {
            "message": "Deleted!",
            "arrayAtual": developers
        }


api.add_resource(Devs, '/devs/')
api.add_resource(Dev, '/devs/<int:indice>')
api.add_resource(Skills, '/skills/')

if __name__ == '__main__':
    app.run(debug=True)