# Escreva uma função que faça a verificação de existência de um item em uma lista.
# A função deve retornar False caso o item não exista ou o próprio item caso ele exista.
dados_pessoais = [1, 2, 3, 4, 5]

item =int(input("Digite o item para procurar\n"))


def verifica_item(dados_pessoais, item):
    if item in dados_pessoais:
        print (dados_pessoais [item])
    else:
        print(False)
    

verifica_item(dados_pessoais, item)