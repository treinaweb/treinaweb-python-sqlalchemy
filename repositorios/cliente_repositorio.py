from dominios.db import Cliente
from fabricas import fabrica_conexao
from queries import cliente_query


class ClienteRepositorio():

    def listar_clientes(self):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM cliente")
            print(cursor.fetchall())
        finally:
            conexao.close()


    def inserir_cliente(self, cliente, sessao):
        query_cliente = cliente_query.ClienteQuery()
        novo_cliente = Cliente(nome=cliente.nome, idade=cliente.idade)
        query_cliente.inserir_cliente(novo_cliente, sessao)

    def editar_cliente(self, id_cliente, cliente):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("UPDATE cliente SET nome=%(nome)s, idade=%(idade)s WHERE idcliente=%(id_cliente)s",
                       ({'nome': cliente.nome, 'idade': cliente.idade, 'id_cliente': id_cliente}))
        finally:
            conexao.close()

    def remover_cliente(self, id_cliente):
        fabrica = fabrica_conexao.FabricaConexao()
        conexao = fabrica.conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM cliente WHERE idcliente=%s", (id_cliente,))
        finally:
            conexao.close()