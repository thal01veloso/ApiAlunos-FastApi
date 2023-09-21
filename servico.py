import requests


def mostarAlunos(instance):
    response = requests.get("http://127.0.0.1:8000/alunos").text
    return print(response)