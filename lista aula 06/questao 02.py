#Faça o mesmo que que se pede na questão anterior
#mas a terceira lista não pode ter itens repetidos.

lista1 = [int(input("Lista 1: ")) for i in range(5)]
lista2 = [int(input("Lista 2: ")) for i in range(5)]


def lista_final(lista1,lista2):
    lista3 = lista1+lista2
    lista4 = []
    for i in lista3:
        if i not in lista4:
            lista4.append(i)
    print(lista4)

lista_final(lista1,lista2)