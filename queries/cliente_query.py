from dominios.db import Cliente


class ClienteQuery():
    def inserir_cliente(self, cliente, sessao):
        sessao.add(cliente)

    def editar_cliente(self, id_cliente, cliente, sessao):
        client = self.listar_cliente_id(id_cliente, sessao)
        client.nome = cliente.nome
        client.idade = cliente.idade
        # sessao.query(Cliente).filter(Cliente.id==id_cliente).update({'nome': cliente.nome, 'idade': cliente.idade})

    def remover_cliente(self, id_cliente, sessao):
        cliente = self.listar_cliente_id(id_cliente, sessao)
        sessao.delete(cliente)

    def listar_clientes(self, sessao):
        clientes = sessao.query(Cliente).all()

        return clientes

    def listar_cliente_id(self, id_cliente, sessao):
        cliente = sessao.query(Cliente).filter(Cliente.id == id_cliente).first()

        return cliente

    def listar_cliente_nome(self, nome_cliente, sessao):
        clientes = sessao.query(Cliente).filter(Cliente.nome == nome_cliente).all()

        return clientes

    def listar_cliente_nome_ordenado(self, nome_cliente, sessao):
        clientes = sessao.query(Cliente).filter(Cliente.nome == nome_cliente).order_by(Cliente.idade.desc()).all()

        return clientes