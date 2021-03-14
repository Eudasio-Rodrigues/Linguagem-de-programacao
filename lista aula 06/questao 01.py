#Faça uma função que receba duas listas e que gere 
#uma terceira com os elementos das duas primeiras.

lista1 = [int(input("Lista 1: ")) for i in range(5)]
lista2 = [int(input("Lista 2: ")) for i in range(5)]


def lista_final(lista1,lista2):
    lista3 = []
    lista3.extend(lista1)
    lista3.extend(lista2)
    lista3 = sorted(lista3)
    print(f"{lista3}")

lista_final(lista1,lista2)