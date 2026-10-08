# 📦 Controle de Estoque API

API REST desenvolvida em **Python** com **FastAPI** para gerenciamento de produtos em um sistema de controle de estoque.

Este projeto faz parte do meu portfólio profissional e demonstra conhecimentos em **desenvolvimento de APIs, operações CRUD, banco de dados, validação de dados e organização de código**.

---

## 🚀 Tecnologias utilizadas

* 🐍 **Python**
* ⚡ **FastAPI**
* 🗄️ **SQLite**
* ✅ **Pydantic**
* 🚀 **Uvicorn**
* 🔧 **Git e GitHub**
* 📚 **Swagger / OpenAPI**

---

## ⚙️ Funcionalidades

A API permite realizar as principais operações de gerenciamento de produtos:

* ✅ Cadastrar produtos
* ✅ Listar produtos
* ✅ Consultar produto por ID
* ✅ Atualizar produtos
* ✅ Excluir produtos
* ✅ Validar dados enviados pela API
* ✅ Retornar códigos HTTP adequados
* ✅ Armazenar informações em banco de dados SQLite
* ✅ Documentar automaticamente os endpoints com Swagger/OpenAPI

---

## 📌 Endpoints

| Método | Endpoint                 | Descrição                          |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/`                      | Verifica se a API está funcionando |
| GET    | `/produtos`              | Lista todos os produtos            |
| GET    | `/produtos/{produto_id}` | Consulta um produto por ID         |
| POST   | `/produtos`              | Cadastra um novo produto           |
| PUT    | `/produtos/{produto_id}` | Atualiza um produto                |
| DELETE | `/produtos/{produto_id}` | Exclui um produto                  |

---

## 📚 Documentação da API

O FastAPI disponibiliza documentação interativa automaticamente através do **Swagger UI**.

Após iniciar a aplicação, acesse:

```text
http://127.0.0.1:8000/docs
```

Também é possível consultar a especificação OpenAPI:

```text
http://127.0.0.1:8000/openapi.json
```

---

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

### 7. Acessar a documentação

Abra no navegador:

```text
http://127.0.0.1:8000/docs
```

---

## 🗂️ Estrutura do projeto

```text
controle-estoque-api/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── produtos.py
│   └── schemas.py
│
├── database/
│   ├── __init__.py
│   ├── database.py
│   └── tabelas.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 💡 O que este projeto demonstra

Este projeto demonstra conhecimentos práticos em:

* Desenvolvimento de APIs REST
* Python e FastAPI
* Operações CRUD
* Integração com banco de dados SQLite
* Validação de dados com Pydantic
* Tratamento de requisições HTTP
* Documentação de APIs
* Organização de projetos Python
* Git e GitHub

---

## 🎯 Objetivo do projeto

O objetivo foi desenvolver uma aplicação prática para consolidar conhecimentos em **desenvolvimento backend e APIs REST**, utilizando tecnologias presentes no mercado e aplicando conceitos de organização e estruturação de código.

---

## 👩‍💻 Sobre mim

Sou **estudante do último ano de Análise e Desenvolvimento de Sistemas** e estou construindo minha carreira na área de Tecnologia.

Tenho interesse em oportunidades como **Desenvolvedora Júnior**, especialmente em posições relacionadas a **Python, backend, APIs REST, automação e desenvolvimento de sistemas**.

---

⭐ Se este projeto foi útil ou interessante para você, fique à vontade para explorar o repositório!
