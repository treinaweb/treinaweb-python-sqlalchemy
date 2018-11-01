from dominios.db import Produto


class ProdutoQuery():
    def inserir_produto(self, novo_produto, sessao):
        sessao.add(novo_produto)

    def listar_produto_id(self, id_produto, sessao):
        produto = sessao.query(Produto).filter(Produto.id == id_produto).first()

        return produto