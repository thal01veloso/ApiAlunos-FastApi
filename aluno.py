from pydantic import BaseModel

class Aluno(BaseModel):
    cpf: str
    nome: str
    dataNascimento: str