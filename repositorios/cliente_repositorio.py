from dominios.db import Cliente
from fabricas import fabrica_conexao
from queries import cliente_query


class ClienteRepositorio():

    def listar_clientes(self, sessao):
        query_cliente = cliente_query.ClienteQuery()
        clientes = query_cliente.listar_clientes(sessao)

        return clientes


    def inserir_cliente(self, cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        novo_cliente = Cliente(nome=cliente.nome, idade=cliente.idade)
        query_cliente.inserir_cliente(novo_cliente, sessao)

    def editar_cliente(self, id_cliente, cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        query_cliente.editar_cliente(id_cliente, cliente, sessao)


    def remover_cliente(self, id_cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        query_cliente.remover_cliente(id_cliente, sessao)