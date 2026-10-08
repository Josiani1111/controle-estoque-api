from database.database import conectar


def listar_produtos():
    conexao = conectar()

    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        return cursor.fetchall()
    finally:
        conexao.close()


def cadastrar_produto(nome, categoria, quantidade, preco):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            INSERT INTO produtos (nome, categoria, quantidade, preco)
            VALUES (?, ?, ?, ?)
            """,
            (nome, categoria, quantidade, preco)
        )

        produto_id = cursor.lastrowid

        conexao.commit()

        return produto_id
    finally:
        conexao.close()


def excluir_produto(produto_id):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "DELETE FROM produtos WHERE id = ?",
            (produto_id,)
        )

        conexao.commit()
    finally:
        conexao.close()


def atualizar_produto(produto_id, nome, categoria, quantidade, preco):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            """
            UPDATE produtos
            SET nome = ?, categoria = ?, quantidade = ?, preco = ?
            WHERE id = ?
            """,
            (nome, categoria, quantidade, preco, produto_id)
        )

        conexao.commit()
    finally:
        conexao.close()


def buscar_produto(produto_id):
    conexao = conectar()

    try:
        cursor = conexao.cursor()

        cursor.execute(
            "SELECT * FROM produtos WHERE id = ?",
            (produto_id,)
        )

        return cursor.fetchone()
    finally:
        conexao.close()