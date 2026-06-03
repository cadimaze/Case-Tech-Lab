from fastapi import FastAPI, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import os
import re

from models import Pessoa

app = FastAPI(
    title="Sistema de Gestão de Pessoas",
    description="API REST para cadastro e gestão de informações de pessoas.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500", "http://localhost:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)

_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_pessoas: List[Pessoa] = []


@app.get("/", include_in_schema=False)
def frontend():
    html_path = os.path.join(_BASE_DIR, "static", "index.html")
    with open(html_path, encoding="utf-8") as f:
        return HTMLResponse(content=f.read())


def _normalizar_cpf(cpf: str) -> str:
    digits = re.sub(r"\D", "", cpf)
    if len(digits) == 11:
        return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"
    return cpf


def _encontrar_pessoa(cpf: str) -> tuple[int, Pessoa]:
    cpf_normalizado = _normalizar_cpf(cpf)
    for index, pessoa in enumerate(db_pessoas):
        if pessoa.cpf == cpf_normalizado:
            return index, pessoa
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Pessoa não encontrada.",
    )


@app.post("/pessoas/", status_code=status.HTTP_201_CREATED)
def cadastrar_pessoa(pessoa: Pessoa):
    for p in db_pessoas:
        if p.cpf == pessoa.cpf:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Já existe uma pessoa cadastrada com este CPF.",
            )
    db_pessoas.append(pessoa)
    return {"msg": "Pessoa cadastrada com sucesso!"}


@app.get("/pessoas/", response_model=List[Pessoa])
def listar_pessoas():
    return db_pessoas


@app.get("/pessoas/{cpf}", response_model=Pessoa)
def obter_pessoa(cpf: str):
    _, pessoa = _encontrar_pessoa(cpf)
    return pessoa


@app.put("/pessoas/{cpf}")
def atualizar_pessoa(cpf: str, pessoa_atualizada: Pessoa):
    index, _ = _encontrar_pessoa(cpf)
    db_pessoas[index] = pessoa_atualizada
    return {"msg": "Pessoa atualizada com sucesso!"}


@app.delete("/pessoas/{cpf}")
def excluir_pessoa(cpf: str):
    index, _ = _encontrar_pessoa(cpf)
    del db_pessoas[index]
    return {"msg": "Pessoa excluída com sucesso!"}
