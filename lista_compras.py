# lista_compras.py

compras = []

while True:
    print("\n=== MENU DE OPÇÕES ===")
    print("1 - Adicionar a lista")
    print("2 - Pesquisar item")
    print("3 - Remover item")
    print("4 - Alterar item")
    print("5 - Listar produtos")
    print("6 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        print("\n--- Adicionar Produtos ---")
        while True:
            produto = input("Digite o produto para adicionar (ou 'sair' para voltar): ").lower()
            if produto == 'sair':
                break
            compras.append(produto)
            print(f"'{produto}' adicionado com sucesso.")
            
    elif opcao == '2':
        print("\n--- Pesquisar Produto ---")
        produto = input("Digite o produto a ser pesquisado: ").lower()
        if produto in compras:
            print(f"Produto encontrado: {produto}")
        else:
            print("Produto não encontrado.")
            
    elif opcao == '3':
        print("\n--- Remover Produto ---")
        produto = input("Digite o nome do produto a ser removido: ").lower()
        if produto in compras:
            compras.remove(produto)
            print("Produto encontrado e removido com sucesso.")
        else:
            print("Produto não encontrado.")
            
    elif opcao == '4':
        print("\n--- Alterar Produto ---")
        produto = input("Digite o nome do produto a ser alterado: ").lower()
        if produto in compras:
            novo_produto = input("Digite o novo nome do produto: ").lower()
            # Encontra o índice (posição) do produto antigo e o substitui
            indice = compras.index(produto)
            compras[indice] = novo_produto
            print("Produto alterado com sucesso.")
        else:
            print("Produto não encontrado.")
            
    elif opcao == '5':
        print("\n--- Lista de Produtos ---")
        if len(compras) == 0:
            print("Lista vazia.")
        else:
            for item in compras:
                print(f"- {item}")
                
    elif opcao == '6':
        print("\nPrograma encerrado com sucesso!")
        break
        
    else:
        print("Opção inválida. Tente novamente.")
