# MENU DO SISTEMA HORTIFRUTI

import textwrap

# LISTA GLOBAL DE PRODUTOS
produtos = []

def menu():
    menu = """\t 
     -------------- MENU -------------- 

        [1]\tCadastrar Produto
        [2]\tListar Produtos
        [3]\tAtualizar produto
        [4]\tRegistrar venda
        [5]\tMostrar relatório
        [6]\tSair
    """
    return input(textwrap.dedent(menu))

def cadastrar_produto():
    print("Cadastrar Produto")
    print("=================")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produto = {"nome": nome, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!\n")

def listar_produtos():
    print("Listar Produtos")
    print("=================")
    if not produtos:
        print("Nenhum produto cadastrado.\n")
    else:
        for i, produto in enumerate(produtos, 1):
            print(f"{i}. Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Quantidade: {produto['quantidade']}")
    print("=================")

# LOOP PRINCIPAL DO SISTEMA
while True:
    opcao = menu()
    if opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "6":
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")
        break
