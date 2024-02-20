# Sistema de Gestão de Pessoas

Este projeto implementa uma API REST simples para o cadastro e gestão de informações de pessoas, permitindo operações básicas como cadastro, consulta, atualização e exclusão de registros (CRUD).

## Tecnologias Utilizadas

- Python 3.12
- FastAPI
- Uvicorn para servir a aplicação
- Swagger UI para documentação da API

## Funcionalidades

- Cadastro de pessoas
- Consulta de pessoas cadastradas
- Atualização dos dados cadastrais
- Exclusão de registros

## Estrutura do Projeto

projeto/
│
├── app/
│ ├── init.py
│ ├── main.py # Arquivo principal contendo a lógica da API
│ └── models.py # Definições dos modelos de dados
│
└── README.md


## Como Configurar

Para configurar este projeto em seu ambiente local, siga estes passos:

1. Clone o repositório para sua máquina local:

git clone https://github.com/cadimaze/Case-Tech-Lab.git


2. Acesse o diretório do projeto:

cd D:\Projetos DEV\CaseBackEndTEchLabs


3. (Opcional) Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate (No Windows use venv\Scripts\activate)


4. Instale as dependências necessárias:

pip install -r requirements.txt


## Como Executar

Para executar a aplicação, use o seguinte comando:

uvicorn app.main:app --reload


A aplicação estará acessível em: `http://127.0.0.1:8000`.
Os endpoints disponíveis podem ser vistos e até mesmo testados diretamente pelo navegador em: 'http://127.0.0.1:8000/docs'.
Esta é outra forma de visualizar a documentação, com um estilo diferente: 'http://127.0.0.1:8000/redoc'

Você pode acessar a documentação da API e testar os endpoints usando a interface do Swagger UI em: `http://127.0.0.1:8000/docs`.

## Contribuições

Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto, sinta-se à vontade para criar um pull request.

## Licença

[MIT](LINK_PARA_SUA_LICENCA)
