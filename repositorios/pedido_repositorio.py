from dominios.db import Pedido
from queries import pedido_query, produto_query
from repositorios import cliente_repositorio


class PedidoRepositorio():
    def inserir_pedido(self, id_cliente, sessao, produtos):
        repositorio_cliente = cliente_repositorio.ClienteRepositorio()
        query_pedido = pedido_query.PedidoQuery()
        query_produto = produto_query.ProdutoQuery()
        cliente = repositorio_cliente.listar_cliente_id(id_cliente, sessao)
        novo_pedido = Pedido(cliente=cliente)
        for i in produtos:
            produto = query_produto.listar_produto_id(i, sessao)
            novo_pedido.produtos.append(produto)
        query_pedido.inserir_pedido(novo_pedido, sessao)
