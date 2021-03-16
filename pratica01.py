def retorna_lista (lista):
    lista[4]=50
    return lista

print(retorna_lista(lista))
lista = ['Eudasio',27, 1.75,1994,'mombaça']

def fatiamento(lista, n1, n2, n3):
    print(lista[0:3])

fatiamento(lista,2,3,1)

impares = [x for x in range(1,10) if x % 2 != 0]
print(impares)

lista = ['Eudasio',27, 1.75,1994,'mombaça']
lista2= tuple(lista)
lista3=list(lista2)
lista3.append("masculino")
lista4=tuple(lista3)
print(lista4)