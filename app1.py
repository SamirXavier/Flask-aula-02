from flask import Flask, jsonify, request

class APIS:
    def __init__(self):
        self.app = Flask(__name__)
        self.alunos= []
        self.setup_routes()
    
    def setup_routes(self):
        @self.app.route("/")
        def index():
            return "working"

        @self.app.route("/api/create", methods=['POST'])
        def aluno():
            if request.method == 'POST':
                aluno = request.json
                self.alunos.append(aluno)
                response = {"success": True, "message": "aluno Salvo com sucesso!"}
                return jsonify(response), 201

        @self.app.route('/api/read', methods=['GET'])
        def aluno_listar():
            return jsonify(self.alunos)
        
        @self.app.route('/api/update/<int:id>', methods=['POST'])
        def aluno_update(id):
            if request.method == 'POST':
                if id -1 < len(self.alunos):
                    aluno = request.json
                    
                    self.alunos[id-1].update(aluno)
                    response = {"success": True, "message": "aluno Salvo com sucesso!"}
                    return jsonify(response), 201
                else:
                    return {"sucess": False, "message" : "ID não existe"}, 400
        
        @self.app.route('/api/delete/<int:id>', methods=['POST'])
        def aluno_delete(id):
            if request.method == 'POST':
                if id -1 < len(self.alunos):
                    
                    self.alunos.pop(id-1)
                    response = {"success": True, "message": "aluno Deletado com sucesso!"}
                    return jsonify(response), 201
                
                else:
                    return {"sucess": False, "message" : "ID não existe"}, 400
        
        @self.app.route('/api/imprimir', methods=[])            
    def run(self):
        self.app.run(debug=True)
        
        

if __name__ == "__main__" :
    api = APIS()
    api.run()