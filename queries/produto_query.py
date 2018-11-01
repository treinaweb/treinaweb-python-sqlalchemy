
class ProdutoQuery():
    def inserir_produto(self, novo_produto, sessao):
        sessao.add(novo_produto)