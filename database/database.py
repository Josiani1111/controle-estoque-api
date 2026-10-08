import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
BANCO = BASE_DIR / "estoque.db"


def conectar():
    """
    Cria e retorna uma conexão com o banco de dados SQLite.
    """
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row

    return conexao