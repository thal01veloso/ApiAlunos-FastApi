from fastapi import FastAPI, HTTPException
from alunoBD import BancoAluno
from aluno import Aluno


app = FastAPI()
bancoDados = BancoAluno()

@app.get("/alunos")
def getAluno():
    return bancoDados.db.all()
@app.get("/procurarCPF")
def getByCPF(cpf):
   return bancoDados.db.search(bancoDados.query.cpf == str(cpf))

@app.post("/cadastroAlunos")
def postAluno(aluno: Aluno):
   try:
        if bancoDados.db.contains(bancoDados.query.cpf == aluno.cpf):
            raise HTTPException(status_code=400, detail="CPF já cadastrado")
        bancoDados.db.insert(dict(aluno))
        return {"message": "Aluno cadastrado com sucesso"}
   except Exception as e:
        return f"Erro ao cadastrar aluno: {str(e)}"

@app.delete("/deletarAluno")
def deleteAluno(cpf):
  return bancoDados.db.remove(bancoDados.query.cpf == str(cpf))

@app.put("/atualizarAluno")
def atualizarAluno(cpf:str, aluno: Aluno):
    try:
      bancoDados.db.update(aluno, bancoDados.query.cpf == str(cpf))
      alunoAtualizado = bancoDados.db.search(bancoDados.query.cpf == str(cpf))
      return alunoAtualizado
    except Exception as e:
        return f"Erro ao atualizar aluno: {str(e)}"
     

   

