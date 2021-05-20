from flask import Flask, request
from flask_restful import Resource, Api
from models import Clientes

app = Flask(__name__)
api = Api(app)


class Cliente(Resource):
    def get(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': cliente.nome,
                'contato': cliente.contato,
                'id': cliente.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa nao encontrada'
            }
        return response

    def put(self, nome):
        cliente = Clientes.query.filter_by(id=id).first()
        dados = request.json
        if 'nome' in dados:
            cliente.nome = dados['nome']
        if 'contato' in dados:
            cliente.contato = dados['contato']
        cliente.save()
        response = {
            'id': cliente.id,
            'nome': cliente.nome,
            'contato': cliente.contato
        }
        return response

    def delete(self, nome):
        cliente = Clientes.query.filter_by(nome=nome).first()
        mensagem = 'Cliente {} excluida com sucesso'.format(cliente.nome)
        cliente.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaClientes(Resource):

    def get(self):
        cliente = Clientes.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'contato': i.contato} for i in cliente]
        return response

    def post(self):
        dados = request.json
        cliente = Clientes(nome=dados['nome'], contato=dados['contato'])
        cliente.save()
        response = {
            'id': cliente.id,
            'nome': cliente.nome,
            'contato': cliente.contato
        }
        return response



api.add_resource(Cliente, '/clientes/<string:nome>/')
api.add_resource(ListaClientes, '/clientes/')


if __name__ == '__main__':
    app.run(debug=True)
