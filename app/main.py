from fastapi import FastAPI, HTTPException
from app.produtos import (

    listar_produtos,
    cadastrar_produto,
    excluir_produto,
    atualizar_produto,
    buscar_produto
)
   
from app.schemas import Produto


app = FastAPI(title="Controle de Estoque API")


@app.get("/")
def inicio():
    return {"mensagem": "API de Controle de Estoque funcionando!"}


@app.get("/produtos")
def produtos():
    return [dict(produto) for produto in listar_produtos()]


@app.post(
    "/produtos",
    status_code=201,
    responses={
        201: {"description": "Produto criado com sucesso"}
    }
)
def criar_produto(produto: Produto):
    produto_id = cadastrar_produto(
        produto.nome,
        produto.categoria,
        produto.quantidade,
        produto.preco
    )

    return {
        "mensagem": "Produto cadastrado com sucesso!",
        "produto": {
            "id": produto_id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "quantidade": produto.quantidade,
            "preco": produto.preco
        }
    }


@app.delete(
    "/produtos/{produto_id}",
    responses={
        404: {"description": "Produto não encontrado"}
    }
)
def deletar_produto(produto_id: int):
    produto = buscar_produto(produto_id)

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    excluir_produto(produto_id)

    return {
        "mensagem": "Produto excluído com sucesso!"
    }    


@app.put(
    "/produtos/{produto_id}",
    responses={
        404: {"description": "Produto não encontrado"}
    }
)
def atualizar_produto_api(produto_id: int, produto: Produto):
    produto_existente = buscar_produto(produto_id)

    if produto_existente is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    atualizar_produto(
        produto_id,
        produto.nome,
        produto.categoria,
        produto.quantidade,
        produto.preco
    )

    return {
        "mensagem": "Produto atualizado com sucesso!",
        "produto": {
            "id": produto_id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "quantidade": produto.quantidade,
            "preco": produto.preco
        }
    }

@app.get(
    "/produtos/{produto_id}",
    responses={
        404: {"description": "Produto não encontrado"}
    }
)
def obter_produto(produto_id: int):
    produto = buscar_produto(produto_id)

    if produto is None:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado"
        )

    return dict(produto)