from flask import Flask, jsonify
import random

app = Flask(__name__)

frases = [
    "Acredite no seu caminho, mesmo quando ele parecer difícil.",
    "Você é mais forte do que imagina.",
    "Grandes mudanças começam com pequenos passos.",
    "Não desista, o recomeço também é parte do sucesso.",
    "Hoje é um bom dia para tentar de novo.",
    "Coragem é seguir, mesmo com medo.",
    "O esforço de hoje constrói o amanhã que você quer.",
    "Seja persistente, não perfeito.",
    "Você está exatamente onde precisa estar para começar.",
    "Cada desafio é uma chance de crescer."
    ]


@app.route("/")
def index():
    return "Working"


@app.route("/api/teste", methods=['GET'])
def teste():
    return jsonify({"success": True})


@app.route("/api/frase", methods=['GET'], defaults = {"id" : None})
@app.route("/api/frase/<int:id>", methods=['GET'])
def get_frase(id):
    if not id:
        frase_sorteada = random.choice(frases)
    elif id -1 < len(frases):
        frase_sorteada = frases[id-1]

    else:
        return {"sucess": False, "message" : "ID não existe"}, 400
        
    response = {"frase" : frase_sorteada}
    return jsonify(response)




@app.route("/api/frases", methods=['GET'])
def get_frases():
    #response = []
    #i = 0
    #for frase in frases:
        #Frase = {f"frase {i}" : frase}
        #i += 1
        #response.append(Frase)
    response = frases
        
    return jsonify(response)
    





if __name__ == "__main__" :
    app.run(debug=True)

