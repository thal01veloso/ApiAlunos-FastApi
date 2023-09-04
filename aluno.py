from pydantic import BaseModel

class Aluno(BaseModel):
    id: int
    cpf: str
    nome: str
    dataNascimento: str