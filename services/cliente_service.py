from database.connection import get_connection
from datetime import datetime


def criar_cliente(nome, cpf, telefone, email):
    conn = get_connection()
    cursor = conn.cursor()

    data_cadastro = datetime.now().isoformat()

    cursor.execute("""
        INSERT INTO clientes (nome, cpf, telefone, email, data_cadastro)
        VALUES (?, ?, ?, ?, ?)
    """, (nome, cpf, telefone, email, data_cadastro))

    conn.commit()
    conn.close()

    print("Cliente cadastrado com sucesso.")


def listar_clientes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()

    conn.close()
    return resultado


def buscar_cliente_por_id(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes WHERE id = ?", (cliente_id,))
    resultado = cursor.fetchone()

    conn.close()
    return resultado


def remover_cliente(cliente_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM clientes WHERE id = ?", (cliente_id,))
    conn.commit()
    conn.close()