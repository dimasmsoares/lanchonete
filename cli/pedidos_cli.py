from cli.menu import exibir_menu
from services.pedido_service import (
    criar_pedido,
    adicionar_item,
    finalizar_pedido,
    listar_pedidos
)


def menu_pedidos():
    opcoes = {
        1: ("Criar novo pedido", novo_pedido),
        2: ("Adicionar item ao pedido", adicionar),
        3: ("Finalizar pedido", finalizar),
        4: ("Listar pedidos", listar)
    }

    exibir_menu("MENU PEDIDOS", opcoes)


def novo_pedido():
    cliente = input("ID cliente (Enter para anônimo): ")
    funcionario = int(input("ID funcionário: "))

    cliente_id = int(cliente) if cliente else None

    pedido_id = criar_pedido(cliente_id, funcionario)
    print(f"Pedido criado com ID {pedido_id}")


def adicionar():
    pedido_id = int(input("ID pedido: "))
    produto_id = int(input("ID produto: "))
    quantidade = int(input("Quantidade: "))

    adicionar_item(pedido_id, produto_id, quantidade)
    print("Item adicionado.")


def finalizar():
    pedido_id = int(input("ID pedido: "))
    finalizar_pedido(pedido_id)
    print("Pedido finalizado.")


def listar():
    pedidos = listar_pedidos()
    for p in pedidos:
        print(dict(p))