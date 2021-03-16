#Faça uma função que receba uma lista e 3 números, esses números devem ser 
#índices válidos dessa lista. A função deve retornar uma tupla composta 
#pelos valores dos índices indicados.

def converte(lista): 
    return tuple(lista) 
   
lista = [1, 2, 3] 
converte(lista)
print(converte(lista)) 