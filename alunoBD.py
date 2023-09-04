from tinydb import TinyDB, Query

class BancoAluno():
    db = TinyDB('alunos.json')
    query = Query()
