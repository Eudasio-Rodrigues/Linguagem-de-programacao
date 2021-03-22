#Escreva uma função que receba como argumento uma lista e uma tupla
#e retorne um set composto pelas duas coleções.

lista = [x for x in range(0,11)]
tupla = ('eudasio',"mombaca",27)

def converte_set(lista,tupla):
    a = set(lista)
    b = set(tupla)
    print(a|b)

converte_set(lista,tupla)