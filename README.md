# 📦 Controle de Estoque API

API REST desenvolvida em **Python** com **FastAPI** para gerenciamento de produtos em um sistema de controle de estoque.

O projeto foi desenvolvido como parte do meu portfólio profissional, com foco em desenvolvimento de APIs, operações CRUD, banco de dados e organização de código.

## 🚀 Tecnologias utilizadas

* Python
* FastAPI
* SQLite
* Pydantic
* Uvicorn
* Git e GitHub
* Swagger / OpenAPI

## ⚙️ Funcionalidades

A API permite:

* ✅ Cadastrar produtos
* ✅ Listar produtos
* ✅ Consultar produto por ID
* ✅ Atualizar produtos
* ✅ Excluir produtos
* ✅ Validar dados enviados pela API
* ✅ Retornar códigos HTTP adequados
* ✅ Armazenar os dados em banco SQLite

## 📌 Endpoints

| Método | Endpoint                 | Descrição                          |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/`                      | Verifica se a API está funcionando |
| GET    | `/produtos`              | Lista todos os produtos            |
| GET    | `/produtos/{produto_id}` | Consulta um produto                |
| POST   | `/produtos`              | Cadastra um produto                |
| PUT    | `/produtos/{produto_id}` | Atualiza um produto                |
| DELETE | `/produtos/{produto_id}` | Exclui um produto                  |

## 🧪 Documentação da API

O projeto utiliza a documentação automática do **Swagger**, disponibilizada pelo FastAPI.

Após iniciar a aplicação, acesse:

```text
http://127.0.0.1:8000/docs
```

Também é possível acessar a especificação OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

## ▶️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Josiani1111/controle-estoque-api.git
```

### 2. Acessar a pasta

```bash
cd controle-estoque-api
```

### 3. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 4. Ativar o ambiente virtual no Windows

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 6. Iniciar a API

```bash
uvicorn app.main:app --reload
```

Depois, abra:
