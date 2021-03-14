#Escreva uma função que receba uma lista com itens repetidos e retorne a
# mesma lista com itens únicos

lista = [1,2,2,5,9,0,0,0,10,3,3,3,3]

def remove_repetidos(lista):
    lista = sorted(set(lista))
    print(lista)

remove_repetidos(lista)