from database import conectar


def criar_tabelas():
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS produtos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                quantidade INTEGER NOT NULL,
                preco REAL NOT NULL
            )
        """)

        conexao.commit()

    finally:
        conexao.close()


if __name__ == "__main__":
    criar_tabelas()
    print("Banco de dados e tabela criados com sucesso!")