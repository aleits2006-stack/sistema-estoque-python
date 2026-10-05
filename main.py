# ============================================================
# SISTEMA DE ESTOQUE
# Projeto de portfólio - Alexandre Ikemoto
# Versão 1.0
# ============================================================

produtos = []


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def encontrar_produto(codigo):
    """Procura um produto pelo código."""

    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto

    return None


def pausar():
    """Pausa o sistema até o usuário pressionar ENTER."""

    input("\nPressione ENTER para continuar...")


# ============================================================
# CADASTRAR PRODUTO
# ============================================================

def cadastrar_produto():
    print("\n" + "=" * 50)
    print("CADASTRO DE PRODUTO")
    print("=" * 50)

    codigo = input("Código do produto: ").strip()

    if encontrar_produto(codigo):
        print("\n❌ Já existe um produto com esse código.")
        pausar()
        return

    nome = input("Nome do produto: ").strip()
    categoria = input("Categoria: ").strip()
    localizacao = input("Localização: ").strip()

    try:
        quantidade = int(input("Quantidade inicial: "))

        if quantidade < 0:
            print("\n❌ A quantidade não pode ser negativa.")
            pausar()
            return

        preco = float(
            input("Preço unitário: R$ ")
            .replace(",", ".")
        )

        if preco < 0:
            print("\n❌ O preço não pode ser negativo.")
            pausar()
            return

    except ValueError:
        print("\n❌ Digite valores numéricos válidos.")
        pausar()
        return

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "localizacao": localizacao,
        "quantidade": quantidade,
        "preco": preco
    }

    produtos.append(produto)

    print("\n✅ Produto cadastrado com sucesso!")
    pausar()


# ============================================================
# LISTAR PRODUTOS
# ============================================================

def listar_produtos():
    print("\n" + "=" * 80)
    print("LISTA DE PRODUTOS")
    print("=" * 80)

    if not produtos:
        print("Nenhum produto cadastrado.")
        pausar()
        return

    for produto in produtos:

        valor_total = (
            produto["quantidade"] *
            produto["preco"]
        )

        print(f"""
Código:       {produto["codigo"]}
Produto:      {produto["nome"]}
Categoria:    {produto["categoria"]}
Localização:  {produto["localizacao"]}
Quantidade:   {produto["quantidade"]}
Preço:        R$ {produto["preco"]:.2f}
Valor estoque:R$ {valor_total:.2f}
-----------------------------------------------
""")

    pausar()


# ============================================================
# BUSCAR PRODUTO
# ============================================================

def buscar_produto():
    print("\n" + "=" * 50)
    print("BUSCAR PRODUTO")
    print("=" * 50)

    codigo = input("Digite o código do produto: ").strip()

    produto = encontrar_produto(codigo)

    if produto is None:
        print("\n❌ Produto não encontrado.")
        pausar()
        return

    print(f"""
Código:       {produto["codigo"]}
Produto:      {produto["nome"]}
Categoria:    {produto["categoria"]}
Localização:  {produto["localizacao"]}
Quantidade:   {produto["quantidade"]}
Preço:        R$ {produto["preco"]:.2f}
""")

    pausar()


# ============================================================
# ENTRADA DE ESTOQUE
# ============================================================

def entrada_estoque():
    print("\n" + "=" * 50)
    print("ENTRADA DE ESTOQUE")
    print("=" * 50)

    codigo = input("Código do produto: ").strip()

    produto = encontrar_produto(codigo)

    if produto is None:
        print("\n❌ Produto não encontrado.")
        pausar()
        return

    try:
        quantidade = int(
            input("Quantidade recebida: ")
        )

        if quantidade <= 0:
            print("\n❌ A quantidade deve ser maior que zero.")
            pausar()
            return

    except ValueError:
        print("\n❌ Digite uma quantidade válida.")
        pausar()
        return

    produto["quantidade"] += quantidade

    print("\n✅ Entrada registrada!")
    print(
        f"Novo estoque: "
        f"{produto['quantidade']} unidades"
    )

    pausar()


# ============================================================
# SAÍDA DE ESTOQUE
# ============================================================

def saida_estoque():
    print("\n" + "=" * 50)
    print("SAÍDA DE ESTOQUE")
    print("=" * 50)

    codigo = input("Código do produto: ").strip()

    produto = encontrar_produto(codigo)

    if produto is None:
        print("\n❌ Produto não encontrado.")
        pausar()
        return

    try:
        quantidade = int(
            input("Quantidade retirada: ")
        )

        if quantidade <= 0:
            print("\n❌ A quantidade deve ser maior que zero.")
            pausar()
            return

    except ValueError:
        print("\n❌ Digite uma quantidade válida.")
        pausar()
        return

    if quantidade > produto["quantidade"]:
        print("\n❌ Estoque insuficiente.")
        print(
            f"Estoque disponível: "
            f"{produto['quantidade']}"
        )
        pausar()
        return

    produto["quantidade"] -= quantidade

    print("\n✅ Saída registrada!")
    print(
        f"Estoque atual: "
        f"{produto['quantidade']} unidades"
    )

    verificar_estoque_baixo(produto)

    pausar()


# ============================================================
# EXCLUIR PRODUTO
# ============================================================

def excluir_produto():
    print("\n" + "=" * 50)
    print("EXCLUIR PRODUTO")
    print("=" * 50)

    codigo = input("Código do produto: ").strip()

    produto = encontrar_produto(codigo)

    if produto is None:
        print("\n❌ Produto não encontrado.")
        pausar()
        return

    print(f"\nProduto encontrado: {produto['nome']}")

    confirmacao = input(
        "Deseja realmente excluir? (s/n): "
    ).lower()

    if confirmacao == "s":

        produtos.remove(produto)

        print("\n✅ Produto excluído com sucesso!")

    else:

        print("\nOperação cancelada.")

    pausar()


# ============================================================
# ESTOQUE BAIXO
# ============================================================

def verificar_estoque_baixo(produto):

    limite = 5

    if produto["quantidade"] <= limite:

        print("\n⚠️ ALERTA DE ESTOQUE BAIXO!")
        print(
            f"Produto: {produto['nome']}"
        )
        print(
            f"Quantidade atual: "
            f"{produto['quantidade']}"
        )


# ============================================================
# PRODUTOS COM ESTOQUE BAIXO
# ============================================================

def listar_estoque_baixo():

    print("\n" + "=" * 50)
    print("PRODUTOS COM ESTOQUE BAIXO")
    print("=" * 50)

    limite = 5

    encontrados = False

    for produto in produtos:

        if produto["quantidade"] <= limite:

            encontrados = True

            print(
                f"""
Código: {produto["codigo"]}
Produto: {produto["nome"]}
Quantidade: {produto["quantidade"]}
Localização: {produto["localizacao"]}
-----------------------------------------
"""
            )

    if not encontrados:

        print(
            "✅ Nenhum produto está com "
            "estoque baixo."
        )

    pausar()


# ============================================================
# RELATÓRIO DE ESTOQUE
# ============================================================

def relatorio_estoque():

    print("\n" + "=" * 60)
    print("RELATÓRIO GERAL DO ESTOQUE")
    print("=" * 60)

    if not produtos:

        print("Nenhum produto cadastrado.")
        pausar()
        return

    quantidade_produtos = len(produtos)

    quantidade_total = 0

    valor_total = 0

    for produto in produtos:

        quantidade_total += produto["quantidade"]

        valor_total += (
            produto["quantidade"] *
            produto["preco"]
        )

    print(f"""
Quantidade de produtos cadastrados: {quantidade_produtos}

Quantidade total em estoque: {quantidade_total}

Valor total do estoque:
R$ {valor_total:.2f}
""")

    pausar()


# ============================================================
# MENU PRINCIPAL
# ============================================================

def menu():

    while True:

        print("\n")

        print("=" * 60)
        print("              SISTEMA DE ESTOQUE")
        print("=" * 60)

        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Buscar produto")
        print("4 - Entrada de estoque")
        print("5 - Saída de estoque")
        print("6 - Excluir produto")
        print("7 - Estoque baixo")
        print("8 - Relatório geral")
        print("0 - Sair")

        print("=" * 60)

        opcao = input(
            "Escolha uma opção: "
        ).strip()

        if opcao == "1":

            cadastrar_produto()

        elif opcao == "2":

            listar_produtos()

        elif opcao == "3":

            buscar_produto()

        elif opcao == "4":

            entrada_estoque()

        elif opcao == "5":

            saida_estoque()

        elif opcao == "6":

            excluir_produto()

        elif opcao == "7":

            listar_estoque_baixo()

        elif opcao == "8":

            relatorio_estoque()

        elif opcao == "0":

            print("\nSistema encerrado.")
            print("Obrigado por utilizar o sistema!")

            break

        else:

            print("\n❌ Opção inválida.")

            pausar()


# ============================================================
# INÍCIO DO PROGRAMA
# ============================================================

if __name__ == "__main__":

    menu()
