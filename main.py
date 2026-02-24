from database.setup import create_tables
from cli.menu import exibir_menu
from cli.clientes_cli import menu_clientes
from cli.produtos_cli import menu_produtos
from cli.pedidos_cli import menu_pedidos
from cli.funcionarios_cli import menu_funcionarios


def main():
    create_tables()

    opcoes = {
    1: ("Clientes", menu_clientes),
    2: ("Produtos", menu_produtos),
    3: ("Funcionários", menu_funcionarios),
    4: ("Pedidos", menu_pedidos),
    }

    exibir_menu("SISTEMA LANCHONETE", opcoes)


if __name__ == "__main__":
    main()