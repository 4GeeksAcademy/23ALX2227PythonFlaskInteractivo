from flask import Flask
from flask import Flask, jsonify
from flask import request

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    todos2 = request.get_json()
    todos.append(todos2)    
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[1]
    return jsonify(todos)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)