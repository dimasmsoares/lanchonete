from database.connection import get_connection


def criar_produto(nome, descricao, preco):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO produtos (nome, descricao, preco)
            VALUES (?, ?, ?)
        """, (nome, descricao, preco))

        conn.commit()
        print("Produto cadastrado com sucesso.")

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


def listar_produtos(apenas_ativos=True):
    conn = get_connection()
    cursor = conn.cursor()

    if apenas_ativos:
        cursor.execute("SELECT * FROM produtos WHERE ativo = 1")
    else:
        cursor.execute("SELECT * FROM produtos")

    produtos = cursor.fetchall()
    conn.close()
    return produtos


def buscar_produto_por_id(produto_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos WHERE id = ?", (produto_id,))
    produto = cursor.fetchone()

    conn.close()
    return produto


def atualizar_produto(produto_id, nome, descricao, preco):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE produtos
            SET nome = ?, descricao = ?, preco = ?
            WHERE id = ?
        """, (nome, descricao, preco, produto_id))

        conn.commit()
        print("Produto atualizado com sucesso.")

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


def alterar_status_produto(produto_id, ativo):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE produtos
            SET ativo = ?
            WHERE id = ?
        """, (ativo, produto_id))

        conn.commit()

        if ativo:
            print("Produto ativado.")
        else:
            print("Produto inativado.")

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()