
class ClienteQuery():
    def inserir_cliente(self, cliente, sessao):
        sessao.add(cliente)