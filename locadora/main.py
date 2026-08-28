import os
os.system('cls')
import json
from clientes import cadastrar_cliente
from jogos import cadastrarjogo
from locacoes import adicionarloc
clientess = []
jogoscadastradoss = []
locaçõess = []
while True:
    sel = input("------------------------------\n|1. cadastrar cliente        |\n|2. cadastrar jogo           |\n|3. listar jogos cadastrados |\n|4. listar clientes          |\n|5. realizar uma locação     |\n|6. listar locações          |\n|7. fechar                   |\n------------------------------\n")
    if sel == '1':
        clientes = cadastrar_cliente()
        clientess.append(clientes)
        with open("clientes.json", "w", encoding="utf-8") as arquivo:
            json.dump(clientess, arquivo, ensure_ascii=False)
    elif sel == '2':
        jogoscadastrados = cadastrarjogo()
        jogoscadastradoss.append(jogoscadastrados)
        with open("jogos.json", "w", encoding="utf-8") as arquivo:
            json.dump(jogoscadastradoss, arquivo, ensure_ascii=False)
    elif sel == '3':
        with open("jogos.json", "r", encoding="utf-8") as arquivo:
            jogoscadastradoss = json.load(arquivo)
            print(jogoscadastradoss)
    elif sel == '4':
        with open("clientes.json", "r", encoding="utf-8") as arquivo:
            clientess = json.load(arquivo)
            print(clientess)
    elif sel == '5':
        locações = adicionarloc()
        locaçõess.append(locações)
        with open("locacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(locaçõess, arquivo, ensure_ascii=False)
    elif sel == '6':
        with open("locacoes.json", "r", encoding="utf-8") as arquivo:
            locaçõess = json.load(arquivo)
            print(locaçõess)
    elif sel == '7':
        print("fechando...")
        break