def cadastrarjogo():
    jogoscadastrados = []
    jogo = input("Nome do jogo: ")
    plataforma = input("Plataforma: ")
    gênero = input("Gênero: ")
    valorpordia = input("Valor por dia: ")
    cadjogo = {"Jogo": jogo, "Plataforma": plataforma, "gênero": gênero, "valor por dia": valorpordia}
    jogoscadastrados.append(cadjogo)
    print("Jogo cadastrado!")
    print(cadjogo)
    return jogoscadastrados