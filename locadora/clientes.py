def cadastrar_cliente():
    clientes = []
    nome = input("Qual o nome?")
    número = input("Qual o número?")
    cliente = {"nome": nome, "número": número}
    clientes.append(cliente)
    print("cadastrado com sucesso!")
    return clientes