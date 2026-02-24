from cli.menu import exibir_menu
from services.funcionario_service import (
    criar_funcionario,
    listar_funcionarios,
    buscar_funcionario_por_id,
    atualizar_funcionario,
    alterar_status_funcionario
)


def menu_funcionarios():
    opcoes = {
        1: ("Cadastrar funcionário", cadastrar),
        2: ("Listar funcionários", listar),
        3: ("Buscar por ID", buscar),
        4: ("Atualizar funcionário", atualizar),
        5: ("Ativar/Inativar funcionário", alterar_status)
    }

    exibir_menu("MENU FUNCIONÁRIOS", opcoes)


def cadastrar():
    nome = input("Nome: ")
    cargo = input("Cargo: ")
    salario = float(input("Salário: "))

    criar_funcionario(nome, cargo, salario)


def listar():
    funcionarios = listar_funcionarios(apenas_ativos=False)
    for f in funcionarios:
        print(dict(f))


def buscar():
    funcionario_id = int(input("ID do funcionário: "))
    funcionario = buscar_funcionario_por_id(funcionario_id)

    if funcionario:
        print(dict(funcionario))
    else:
        print("Funcionário não encontrado.")


def atualizar():
    funcionario_id = int(input("ID do funcionário: "))
    nome = input("Novo nome: ")
    cargo = input("Novo cargo: ")
    salario = float(input("Novo salário: "))

    atualizar_funcionario(funcionario_id, nome, cargo, salario)


def alterar_status():
    funcionario_id = int(input("ID do funcionário: "))
    status = input("Digite 1 para ativar ou 0 para inativar: ")

    if status not in ("0", "1"):
        print("Opção inválida.")
        return

    alterar_status_funcionario(funcionario_id, int(status))