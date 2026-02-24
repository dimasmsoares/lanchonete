from database.connection import get_connection

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # TABELA CLIENTES
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cpf TEXT UNIQUE,
        telefone TEXT,
        email TEXT,
        data_cadastro TEXT NOT NULL,
        ativo INTEGER NOT NULL DEFAULT 1,

        CHECK (cpf IS NULL OR length(cpf) = 11)
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_clientes_cpf 
    ON clientes(cpf)
    """)


    # ==========================
    # TABELA FUNCIONÁRIOS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cargo TEXT NOT NULL,
        salario REAL NOT NULL CHECK (salario >= 0),
        ativo INTEGER NOT NULL DEFAULT 1
    )
    """)


    # ==========================
    # TABELA PRODUTOS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        preco REAL NOT NULL CHECK (preco >= 0),
        ativo INTEGER NOT NULL DEFAULT 1
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_produtos_nome
    ON produtos(nome)
    """)


    # ==========================
    # TABELA PEDIDOS
    # cliente_id pode ser NULL
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cliente_id INTEGER NULL,
        funcionario_id INTEGER NOT NULL,
        data_pedido TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'aberto',
        total REAL NOT NULL DEFAULT 0 CHECK (total >= 0),

        FOREIGN KEY (cliente_id) REFERENCES clientes(id)
            ON DELETE SET NULL,

        FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
            ON DELETE RESTRICT,

        CHECK (status IN ('aberto', 'finalizado', 'cancelado'))
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_pedidos_data
    ON pedidos(data_pedido)
    """)


    # ==========================
    # TABELA PEDIDO_ITENS
    # ==========================
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pedido_itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pedido_id INTEGER NOT NULL,
        produto_id INTEGER NOT NULL,
        quantidade INTEGER NOT NULL CHECK (quantidade > 0),
        preco_unitario REAL NOT NULL CHECK (preco_unitario >= 0),
        subtotal REAL NOT NULL CHECK (subtotal >= 0),

        FOREIGN KEY (pedido_id) REFERENCES pedidos(id)
            ON DELETE CASCADE,

        FOREIGN KEY (produto_id) REFERENCES produtos(id)
            ON DELETE RESTRICT
    )
    """)

    cursor.execute("""
    CREATE INDEX IF NOT EXISTS idx_pedido_itens_pedido
    ON pedido_itens(pedido_id)
    """)

    conn.commit()
    conn.close()