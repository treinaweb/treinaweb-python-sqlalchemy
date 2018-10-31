
class PedidoQuery():
    def inserir_pedido(self, pedido, sessao):
        sessao.add(pedido)