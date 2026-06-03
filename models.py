from pydantic import BaseModel, Field, field_validator
from datetime import date
import re


class Pessoa(BaseModel):
    nome_completo: str = Field(..., min_length=3, max_length=150, examples=["João da Silva"])
    data_nascimento: date = Field(..., examples=["1990-01-15"])
    endereco: str = Field(..., min_length=5, max_length=200, examples=["Rua das Flores, 123, São Paulo - SP"])
    cpf: str = Field(..., examples=["123.456.789-09"])
    estado_civil: str = Field(..., examples=["casado"])

    model_config = {"str_strip_whitespace": True}

    @field_validator("cpf")
    @classmethod
    def validar_cpf(cls, v: str) -> str:
        digits = re.sub(r"\D", "", v)
        if len(digits) != 11:
            raise ValueError("CPF deve conter exatamente 11 dígitos.")
        if len(set(digits)) == 1:
            raise ValueError("CPF inválido.")

        def calcular_digito(seq: str, pesos: range) -> int:
            total = sum(int(d) * p for d, p in zip(seq, pesos))
            resto = total % 11
            return 0 if resto < 2 else 11 - resto

        d1 = calcular_digito(digits[:9], range(10, 1, -1))
        d2 = calcular_digito(digits[:10], range(11, 1, -1))

        if d1 != int(digits[9]) or d2 != int(digits[10]):
            raise ValueError("CPF inválido.")

        return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"

    @field_validator("data_nascimento")
    @classmethod
    def validar_data_nascimento(cls, v: date) -> date:
        if v >= date.today():
            raise ValueError("Data de nascimento deve ser uma data no passado.")
        return v

    @field_validator("estado_civil")
    @classmethod
    def validar_estado_civil(cls, v: str) -> str:
        opcoes_validas = {
            "solteiro", "solteira",
            "casado", "casada",
            "divorciado", "divorciada",
            "viúvo", "viúva",
            "separado", "separada",
            "união estável",
        }
        normalizado = v.strip().lower()
        if normalizado not in opcoes_validas:
            raise ValueError(
                f"Estado civil inválido. Valores aceitos: {', '.join(sorted(opcoes_validas))}."
            )
        return normalizado
