#Faça uma função que receba uma lista e 3 números, esses números devem ser 
#índices válidos dessa lista. A função deve retornar uma tupla composta 
#pelos valores dos índices indicados.

numeros = [x for x in range(1,11)]
print(numeros)
def converte(numeros, a ,b, c):
    lista = []
    lista.append(numeros[a])
    lista.append(numeros[b])
    lista.append(numeros[c])
    nova_lista = tuple(lista)
    print(nova_lista)

converte(numeros, 2, 4, 6)