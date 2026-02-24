from cli.menu import exibir_menu
from services.produto_service import (
    criar_produto,
    listar_produtos,
    buscar_produto_por_id,
    atualizar_produto,
    alterar_status_produto
)


def menu_produtos():
    opcoes = {
        1: ("Cadastrar produto", cadastrar),
        2: ("Listar produtos", listar),
        3: ("Buscar produto por ID", buscar),
        4: ("Atualizar produto", atualizar),
        5: ("Ativar/Inativar produto", alterar_status)
    }

    exibir_menu("MENU PRODUTOS", opcoes)


def cadastrar():
    nome = input("Nome: ")
    descricao = input("Descrição: ")
    preco = float(input("Preço: "))

    criar_produto(nome, descricao, preco)


def listar():
    produtos = listar_produtos(apenas_ativos=False)
    for p in produtos:
        print(dict(p))


def buscar():
    produto_id = int(input("ID do produto: "))
    produto = buscar_produto_por_id(produto_id)

    if produto:
        print(dict(produto))
    else:
        print("Produto não encontrado.")


def atualizar():
    produto_id = int(input("ID do produto: "))
    nome = input("Novo nome: ")
    descricao = input("Nova descrição: ")
    preco = float(input("Novo preço: "))

    atualizar_produto(produto_id, nome, descricao, preco)


def alterar_status():
    produto_id = int(input("ID do produto: "))
    status = input("Digite 1 para ativar ou 0 para inativar: ")

    if status not in ("0", "1"):
        print("Opção inválida.")
        return

    alterar_status_produto(produto_id, int(status))