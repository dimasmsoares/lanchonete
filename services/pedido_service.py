from database.connection import get_connection
from datetime import datetime


def criar_pedido(cliente_id, funcionario_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        data_pedido = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO pedidos (cliente_id, funcionario_id, data_pedido, status)
            VALUES (?, ?, ?, 'aberto')
        """, (cliente_id, funcionario_id, data_pedido))

        pedido_id = cursor.lastrowid

        conn.commit()
        return pedido_id

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()

def adicionar_item(pedido_id, produto_id, quantidade):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Buscar preço atual do produto
        cursor.execute("SELECT preco FROM produtos WHERE id = ?", (produto_id,))
        produto = cursor.fetchone()

        if not produto:
            raise ValueError("Produto não encontrado.")

        preco_unitario = produto["preco"]
        subtotal = preco_unitario * quantidade

        # Inserir item
        cursor.execute("""
            INSERT INTO pedido_itens
            (pedido_id, produto_id, quantidade, preco_unitario, subtotal)
            VALUES (?, ?, ?, ?, ?)
        """, (pedido_id, produto_id, quantidade, preco_unitario, subtotal))

        # Atualizar total do pedido
        cursor.execute("""
            UPDATE pedidos
            SET total = total + ?
            WHERE id = ?
        """, (subtotal, pedido_id))

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()

def finalizar_pedido(pedido_id):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE pedidos
            SET status = 'finalizado'
            WHERE id = ? AND status = 'aberto'
        """, (pedido_id,))

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()

def listar_pedidos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.id, p.data_pedido, p.status, p.total,
               c.nome as cliente,
               f.nome as funcionario
        FROM pedidos p
        LEFT JOIN clientes c ON p.cliente_id = c.id
        JOIN funcionarios f ON p.funcionario_id = f.id
        ORDER BY p.data_pedido DESC
    """)

    pedidos = cursor.fetchall()
    conn.close()
    return pedidos