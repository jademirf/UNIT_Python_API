from flask import Flask, jsonify, request
import json

app = Flask(__name__)

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

# Operações realizadas com o array completo sem identificação do dev
@app.route('/devs', methods=['GET', 'POST'])
def devs():
    if request.method == "GET":
        return jsonify(developers)
    elif request.method == "POST":
        newDev = json.loads(request.data)
        developers.append(newDev)
        return jsonify({
            "message": "Created!",
            "newValue": newDev
        })

# Operações com um único dev identificado pelo índice dele na lista
@app.route('/devs/<int:indice>', methods=['GET', 'PUT', 'DELETE'])
def dev(indice):
    try:
        developers[indice]
    except IndexError:
        message = 'Developer ID {} not found!'.format(indice)
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    except:
        message = 'Deu um erro que ninguém faz ideia'
        return jsonify({
            "message": message,
            "status": "Error!"
        })
    # Verifica se o método da requisição é GET
    if request.method == 'GET':
        return developers[indice]
    # Caso não seja GET verifica se é PUT
    elif request.method == 'PUT':
        # newValue recebe os dados do corpo da requisição e passa para o formato json
        newValue = json.loads(request.data)
        # Altera o valor da lista no indice informado com o novo valor recebido
        developers[indice] = newValue
        return jsonify({
            "message": "Updated!",
            "newValue": newValue
        })
    elif request.method == 'DELETE':
        print(indice)
        developers.pop(indice)
        return jsonify({
            "message": "Deleted!",
            "arrayAtual": developers
        })


if __name__ == '__main__':
    app.run(debug=True)