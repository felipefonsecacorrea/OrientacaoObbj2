from bd import Dados 
from flask import Flask, jsonify, make_response, request

app=Flask('dados')

@app.route('/dados',methods=['GET'])

def get_dados():
    return Dados

@app.route('/dados/<int:id>',methods=['GET'])
def get_dados_id(id):
    for dados in Dados:
        if dados.get('id')==id:
            return jsonify(dados)

@app.route('/dados',methods=['POST'])

def get_dados_criar():
    dados = request.json
    Dados.append(dados)
    return make_response(
        jsonify(mesnagem = 'Dados cadastrados', dados = dados)
    )

@app.route('/dados/<int:id>',methods=['PUT'])

def get_dados_editar(id):
    dadosAlterados = request.get_json()
    for indice,dados in enumerate(Dados):
        if dados.get('id') == id:
            Dados[indice].update(dadosAlterados)
            return jsonify(Dados[indice])
        
@app.route('/dados/<int:id>',methods=['DELETE'])
def get_dados_excluir(id):
    for indice,dados in enumerate(Dados):
        if dados.get('id') == id:
            del Dados[indice]
            return jsonify({'mensagem':'Dados excluidos.'})



app.run(port=5000,host='localhost')