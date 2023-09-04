from fastapi import FastAPI
from alunoBD import BancoAluno
from aluno import Aluno


app = FastAPI()
bancoDados = BancoAluno()

@app.get("/alunos")
def getAluno():
    return bancoDados.db.all()
@app.get("/procurarId")
def getById(id):
   return bancoDados.db.search(bancoDados.query.id == id)

@app.post("/cadastroAlunos")
def postAluno(aluno: Aluno):
  aluno = dict(aluno)
  return bancoDados.db.insert(aluno)

@app.delete("/deletarAluno")
def deleteAluno(id):
  return bancoDados.db.remove(bancoDados.query.id == id)
    
   
     

   

