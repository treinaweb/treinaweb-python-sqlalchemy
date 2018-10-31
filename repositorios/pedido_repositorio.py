from dominios.db import Pedido
from queries import pedido_query
from repositorios import cliente_repositorio


class PedidoRepositorio():
    def inserir_pedido(self, id_cliente, sessao):
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        query_pedido = pedido_query.PedidoQuery()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)
        novo_pedido = Pedido(cliente=cliente)
        query_pedido.inserir_pedido(novo_pedido, sessao)
