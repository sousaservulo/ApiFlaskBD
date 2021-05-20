from models import Clientes

# Insere dados na tabela Clientes
def insere_pessoas():
    pessoa = Clientes(nome='Sousa',contato=34)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela Clientes
def consulta_pessoas():
    pessoas = Clientes.query.all()
    print(pessoas)
    pessoa = Clientes.query.filter_by(nome=nome).first()
    print(pessoa.idade)

# Altera dados na tabela Clientes
def altera_pessoa():
    pessoa = Clientes.query.filter_by(id=id).first()
    pessoa.save()

# Exclui dados na tabela Clientes
def exclui_pessoa():
    pessoa = Clientes.query.filter_by(id=id).first()
    pessoa.delete()


def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':


    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()

