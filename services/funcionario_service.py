from database.connection import get_connection


def criar_funcionario(nome, cargo, salario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO funcionarios (nome, cargo, salario)
            VALUES (?, ?, ?)
        """, (nome, cargo, salario))

        conn.commit()
        print("Funcionário cadastrado com sucesso.")

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


def listar_funcionarios(apenas_ativos=True):
    conn = get_connection()
    cursor = conn.cursor()

    if apenas_ativos:
        cursor.execute("SELECT * FROM funcionarios WHERE ativo = 1")
    else:
        cursor.execute("SELECT * FROM funcionarios")

    funcionarios = cursor.fetchall()
    conn.close()
    return funcionarios


def buscar_funcionario_por_id(funcionario_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM funcionarios WHERE id = ?", (funcionario_id,))
    funcionario = cursor.fetchone()

    conn.close()
    return funcionario


def atualizar_funcionario(funcionario_id, nome, cargo, salario):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE funcionarios
            SET nome = ?, cargo = ?, salario = ?
            WHERE id = ?
        """, (nome, cargo, salario, funcionario_id))

        conn.commit()
        print("Funcionário atualizado com sucesso.")

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()


def alterar_status_funcionario(funcionario_id, ativo):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE funcionarios
            SET ativo = ?
            WHERE id = ?
        """, (ativo, funcionario_id))

        conn.commit()

        if ativo:
            print("Funcionário ativado.")
        else:
            print("Funcionário inativado.")

    except Exception as e:
        conn.rollback()
        raise e

    finally:
        conn.close()