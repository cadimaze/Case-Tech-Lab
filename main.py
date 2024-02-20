from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import uuid

app = FastAPI()


class Pessoa(BaseModel):
    id: Optional[str] = None
    nome_completo: str
    data_nascimento: date
    endereco: str
    cpf: str
    estado_civil: str


# Simulando um banco de dados em memória
db: List[Pessoa] = []


@app.get("/")
def read_root():
    return {"message": "Bem-vindo(a) à API de Gestão de Pessoas!"}


@app.post("/pessoas/", response_model=Pessoa)
def create_pessoa(pessoa: Pessoa):
    pessoa.id = str(uuid.uuid4())
    db.append(pessoa)
    return pessoa


@app.get("/pessoas/", response_model=List[Pessoa])
def read_pessoas():
    return db


@app.get("/pessoas/{pessoa_id}", response_model=Pessoa)
def read_pessoa(pessoa_id: str):
    for pessoa in db:
        if pessoa.id == pessoa_id:
            return pessoa
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")


@app.put("/pessoas/{pessoa_id}", response_model=Pessoa)
def update_pessoa(pessoa_id: str, pessoa_atualizada: Pessoa):
    for index, pessoa in enumerate(db):
        if pessoa.id == pessoa_id:
            db[index] = pessoa_atualizada
            db[index].id = pessoa_id  # Garante que o ID permanece o mesmo
            return db[index]
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")


@app.delete("/pessoas/{pessoa_id}", response_model=None)
def delete_pessoa(pessoa_id: str):
    for index, pessoa in enumerate(db):
        if pessoa.id == pessoa_id:
            del db[index]
            return
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")
