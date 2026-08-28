def adicionarloc():
    locações = []
    cliente = input("Cliente: ")
    jogo = input("Jogo: ")
    dias = int(input("Dias: "))
    preco = float(input("Preço: "))
    if dias >= 7:
        desconto = 10
    elif dias >= 4 and dias <= 6:
        desconto = 5
    elif dias <= 3:
        desconto = 0
    preco = preco * dias
    preco = preco - (preco * desconto / 100)
    locacao = {"Cliente": cliente, "Jogo": jogo, "Dias": dias, "Desconto": desconto, "Preço": preco}
    locações.append(locacao)
    print(f"Locação adicionada!\nPreço de {preco} com desconto de {desconto}%")
    return locações
def calcpreço():
    cliente = input("Cliente: ")
