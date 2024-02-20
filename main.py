from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from datetime import date


# Definição do modelo de dados usando Pydantic
class Pessoa(BaseModel):
    nome_completo: str
    data_nascimento: date
    endereco: str
    cpf: str
    estado_civil: str


app = FastAPI()

# Lista para armazenar as pessoas cadastradas (nossa "base de dados" em memória)
db_pessoas: List[Pessoa] = []


# CRUD Endpoints

# Cadastrar uma nova pessoa
@app.post("/pessoas/")
def cadastrar_pessoa(pessoa: Pessoa):
    db_pessoas.append(pessoa)
    return {"msg": "Pessoa cadastrada com sucesso!"}


# Listar todas as pessoas
@app.get("/pessoas/", response_model=List[Pessoa])
def listar_pessoas():
    return db_pessoas


# Obter detalhes de uma pessoa específica pelo CPF
@app.get("/pessoas/{cpf}", response_model=Pessoa)
def obter_pessoa(cpf: str):
    for pessoa in db_pessoas:
        if pessoa.cpf == cpf:
            return pessoa
    return {"msg": "Pessoa não encontrada."}


# Atualizar os dados de uma pessoa
@app.put("/pessoas/{cpf}")
def atualizar_pessoa(cpf: str, pessoa_atualizada: Pessoa):
    for index, pessoa in enumerate(db_pessoas):
        if pessoa.cpf == cpf:
            db_pessoas[index] = pessoa_atualizada
            return {"msg": "Pessoa atualizada com sucesso!"}
    return {"msg": "Pessoa não encontrada."}


# Excluir uma pessoa
@app.delete("/pessoas/{cpf}")
def excluir_pessoa(cpf: str):
    for index, pessoa in enumerate(db_pessoas):
        if pessoa.cpf == cpf:
            del db_pessoas[index]
            return {"msg": "Pessoa excluída com sucesso!"}
    return {"msg": "Pessoa não encontrada."}
