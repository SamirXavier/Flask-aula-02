from flask import Flask, jsonify, request


app = Flask(__name__)

alunos = []

# {"nome":"jhon", "nota": 8}


@app.route("/")
def index():
    return "working"

@app.route("/api/create", methods=['POST'])
def aluno():
    if request.method == 'POST':
        aluno = request.json
        alunos.append(aluno)
        response = {"success": True, "message": "aluno Salvo com sucesso!"}
        return jsonify(response), 201

@app.route('/api/read', methods=['GET'])
def aluno_listar():
    return jsonify(alunos)

if __name__ == "__main__" :
    app.run(debug=True)
