from dominios.db import Cliente


class ClienteQuery():
    def inserir_cliente(self, cliente, sessao):
        sessao.add(cliente)

    def editar_cliente(self, id_cliente, cliente, sessao):
        sessao.query(Cliente).filter(Cliente.id==id_cliente).update({'nome': cliente.nome, 'idade': cliente.idade})

    def remover_cliente(self, id_cliente, sessao):
        cliente = sessao.query(Cliente).filter(Cliente.id==id_cliente).first()
        sessao.delete(cliente)

    def listar_clientes(self, sessao):
        clientes = sessao.query(Cliente).all()

        return clientes