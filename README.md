# Sistema de Gestão de Pessoas

API REST para cadastro e gestão de informações de pessoas, com operações completas de CRUD (Create, Read, Update, Delete).

## Tecnologias

- Python 3.12
- FastAPI
- Pydantic v2
- Uvicorn

## Estrutura do Projeto

```
Case-Tech-Lab/
├── main.py          # Aplicação FastAPI e endpoints
├── models.py        # Modelos de dados com validações
├── requirements.txt # Dependências do projeto
└── README.md
```

## Endpoints

| Método   | Rota             | Descrição                        |
|----------|------------------|----------------------------------|
| `POST`   | `/pessoas/`      | Cadastra uma nova pessoa         |
| `GET`    | `/pessoas/`      | Lista todas as pessoas           |
| `GET`    | `/pessoas/{cpf}` | Retorna uma pessoa pelo CPF      |
| `PUT`    | `/pessoas/{cpf}` | Atualiza os dados de uma pessoa  |
| `DELETE` | `/pessoas/{cpf}` | Remove uma pessoa pelo CPF       |

## Como Configurar

1. Clone o repositório:

```bash
git clone https://github.com/cadimaze/Case-Tech-Lab.git
cd Case-Tech-Lab
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como Executar

```bash
uvicorn main:app --reload
```

A aplicação estará disponível em `http://127.0.0.1:8000`.

- Documentação interativa (Swagger): `http://127.0.0.1:8000/docs`
- Documentação alternativa (ReDoc): `http://127.0.0.1:8000/redoc`

## Validações

- **CPF**: aceita com ou sem formatação, valida os dígitos verificadores pelo algoritmo oficial
- **Data de nascimento**: deve ser uma data no passado
- **Estado civil**: valores aceitos — `solteiro(a)`, `casado(a)`, `divorciado(a)`, `viúvo(a)`, `separado(a)`, `união estável`

## Licença

[MIT](LICENSE.md)
