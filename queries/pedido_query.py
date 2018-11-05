from sqlalchemy.orm import joinedload

from dominios.db import Pedido


class PedidoQuery():
    def inserir_pedido(self, pedido, sessao):
        sessao.add(pedido)

    def listar_pedidos(self, sessao):
        pedidos = sessao.query(Pedido).options(joinedload(Pedido.produtos)).all()

        return pedidos