from repositorios import cliente_repositorio
from entidades import cliente
from fabricas import fabrica_conexao

fabrica = fabrica_conexao.FabricaConexao()
sessao = fabrica.criar_sessao()
nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))
novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
repositorio = cliente_repositorio.ClienteRepositorio()
repositorio.inserir_cliente(novo_cliente, sessao)
sessao.commit()