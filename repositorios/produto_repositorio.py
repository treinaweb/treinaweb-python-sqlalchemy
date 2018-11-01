from dominios.db import Produto
from queries import produto_query


class ProdutoRepositorio():
    def inserir_produto(self, produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        novo_produto = Produto(descricao=produto.descricao, valor=produto.valor)
        query_produto.inserir_produto(novo_produto, sessao)

    def listar_produto_id(self, id_produto, sessao):
        query_produto = produto_query.ProdutoQuery()
        produto = query_produto.listar_produto_id(id_produto, sessao)

        return produto