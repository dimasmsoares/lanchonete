import sqlite3              # Importa o módulo padrão do Python para trabalhar com SQLite.
from pathlib import Path    # Importa a classe Path, usada para manipulação moderna de caminhos de arquivos.

DB_PATH = Path(__file__).parent.parent / "data" / "lanchonete.db"
# __file__ é uma variável especial do Python que contém o caminho do arquivo atual.
# Path(__file__) converte o caminho string em objeto Path.
# .parent volta um nível -> .parent.parent volta dois níveis
# / "data" / "lanchonete.db" o operador / no Path serve para concatenar caminhos.
# Assim o banco sempre será criado dentro da pasta data e funciona em qualquer sistema operacional

def get_connection():                           # Função que centraliza a criação da conexão.
    conn = sqlite3.connect(DB_PATH)             # Abre conexão com o banco. Se o arquivo não existir, cria; se existir, apenas conecta.
    conn.row_factory = sqlite3.Row              # Define o retorno como um objeto tipo dicionário (não uma tupla, padrão).
    conn.execute("PRAGMA foreign_keys = ON;")   # SQLite valida FKs corretamente
    return conn                                 # Retorna a conexão configurada.

