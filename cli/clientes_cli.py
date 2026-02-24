from cli.menu import exibir_menu
from services.cliente_service import (
    criar_cliente,
    listar_clientes,
    buscar_cliente_por_id,
    remover_cliente
)

def menu_clientes():
    opcoes = {
        1: ("Cadastrar cliente", cadastrar),
        2: ("Listar clientes", listar),
        3: ("Buscar cliente por ID", buscar),
        4: ("Remover cliente", remover)
    }

    exibir_menu("MENU CLIENTES", opcoes)


def cadastrar():
    nome = input("Nome (opcional): ") or None
    cpf = input("CPF (opcional): ") or None
    telefone = input("Telefone: ") or None
    email = input("Email: ") or None

    criar_cliente(nome, cpf, telefone, email)


def listar():
    clientes = listar_clientes()
    for cliente in clientes:
        print(dict(cliente))


def buscar():
    cliente_id = int(input("ID do cliente: "))
    cliente = buscar_cliente_por_id(cliente_id)

    if cliente:
        print(dict(cliente))
    else:
        print("Cliente não encontrado.")


def remover():
    cliente_id = int(input("ID do cliente: "))
    remover_cliente(cliente_id)
    print("Cliente removido.")