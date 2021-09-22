import json
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/users/<int:id>')
def users(id):
    return jsonify({"id": id, "name": "Desmennyellysson Jerry", "email": "desmenny123@gmail.com"})

@app.route('/sum', methods=['POST'])
def sumNumbers():
    result = sum(json.loads(request.data)['numbers'])
    return jsonify({"total: ": result})

if __name__ == '__main__':
    app.run(debug=True)