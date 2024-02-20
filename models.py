from pydantic import BaseModel
from datetime import date


class Pessoa(BaseModel):
    nome_completo: str
    data_nascimento: date
    endereco: str
    cpf: str
    estado_civil: str
