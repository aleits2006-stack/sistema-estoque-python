```python
# Sistema de Estoque
# Projeto desenvolvido para estudo de Python

produtos = []


def cadastrar_produto():
    print("\n=== CADASTRO DE PRODUTO ===")

    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    quantidade = int(input("Quantidade: "))

    produto = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    produtos.append(produto)

    print("\nProduto cadastrado com sucesso!")


def listar_produtos():
    print("\n=== PRODUTOS CADASTRADOS ===")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(
            f"Produto: {produto['nome']} | "
            f"Categoria: {produto['categoria']} | "
            f"Quantidade: {produto['quantidade']}"
        )


def menu():
    while True:
        print("\n==============================")
        print("       SISTEMA DE ESTOQUE")
        print("==============================")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("0 - Sair")
        print("==============================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto()

        elif opcao == "2":
            listar_produtos()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


menu()
```
