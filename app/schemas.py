from pydantic import BaseModel, Field


class Produto(BaseModel):
    nome: str = Field(
        min_length=2,
        max_length=100,
        description="Nome do produto"
    )

    categoria: str = Field(
        min_length=2,
        max_length=50,
        description="Categoria do produto"
    )

    quantidade: int = Field(
        ge=0,
        description="Quantidade disponível em estoque"
    )

    preco: float = Field(
        gt=0,
        description="Preço do produto"
    )