from repositorios import cliente_repositorio, pedido_repositorio, produto_repositorio
from entidades import cliente, produto
from fabricas import fabrica_conexao

loop = True
while loop:
    print(30 * "-", "MENU", 30 * "-" )
    print("1. Cliente")
    print("2. Produtos")
    print("3. Pedidos")
    print("0. Sair")
    print(67 * "-")

    menu_principal = int(input("Digite a opção desejada: "))

    if menu_principal == 1:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Inserir cliente")
        print("2. Editar cliente")
        print("3. Remover cliente")
        print("4. Listar cliente nome")
        print("0. Sair")
        print(67 * "-")
        menu_cliente = int(input("Digite a opção desejada: "))

        if menu_cliente == 1:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                nome_cliente = input("Digite o nome do cliente: ")
                idade_cliente = int(input("Digite a idade do cliente: "))
                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.inserir_cliente(novo_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 2:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("ID do cliente a ser atualizado: "))
                nome_cliente = input("Digite o nome do cliente: ")
                idade_cliente = int(input("Digite a idade do cliente: "))
                novo_cliente = cliente.Cliente(nome_cliente, idade_cliente)
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.editar_cliente(id_cliente, novo_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        elif menu_cliente == 3:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o ID do cliente a ser removido"))
                repositorio = cliente_repositorio.ClienteRepositorio()
                repositorio.remover_cliente(id_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_cliente == 4:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                repositorio = cliente_repositorio.ClienteRepositorio()
                # clientes = repositorio.listar_clientes(sessao)
                # for i in clientes:
                #     print(i)
                # cliente = repositorio.listar_cliente_id(5, sessao)
                # print(cliente)
                clientes = repositorio.listar_cliente_nome_ordenado("Maria", sessao)
                for i in clientes:
                    print(i)
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()
        else:
            continue

    elif menu_principal == 2:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Inserir produto")
        print("2. Buscar produto ID")
        print("0. Sair")
        print(67 * "-")
        menu_produto = int(input("Digite a opção desejada: "))

        if menu_produto == 1:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                descricao_produto = input("Digite a descrição do produto: ")
                valor_produto = int(input("Digite o valor do produto: "))
                novo_produto = produto.Produto(descricao_produto, valor_produto)
                repositorio_produto = produto_repositorio.ProdutoRepositorio()
                repositorio_produto.inserir_produto(novo_produto, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_produto == 2:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                id_produto = int(input("Digite o ID do produto a ser pesquisado"))
                repositorio = produto_repositorio.ProdutoRepositorio()
                produto = repositorio.listar_produto_id(id_produto, sessao)
                print(produto)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_produto == 0:
            continue

        else:
            print("Opção inválida")

    elif menu_principal == 3:
        print(30 * "-", "MENU", 30 * "-")
        print("1. Inserir pedido")
        print("0. Sair")
        print(67 * "-")
        menu_pedido = int(input("Digite a opção desejada: "))

        if menu_pedido == 1:
            fabrica = fabrica_conexao.FabricaConexao()
            sessao = fabrica.criar_sessao()
            try:
                id_cliente = int(input("Digite o ID do cliente a ser relacionado com o novo pedido"))
                repositorio_pedido = pedido_repositorio.PedidoRepositorio()
                repositorio_pedido.inserir_pedido(id_cliente, sessao)
                sessao.commit()
            except:
                sessao.rollback()
                raise
            finally:
                sessao.close()

        elif menu_pedido == 0:
            continue

        else:
            print("Opção inválida")


    elif menu_principal == 0:
        print("Até mais!")
        break

    else:
        print("Opção inválida.")