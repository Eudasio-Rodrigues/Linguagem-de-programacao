#Utilizando dic conprehension e list comprehension construa uma função que gere o seguinte dicionário: 
#O dicionario deve ter como chave as letras de um nome inserido como argumento e 
# como valor uma lista de pares dentro de um range, passado também como argumento
lista_pares =[ x for x in range (0,11) if x%2==0]
nome='eudasio'
def dicionario(nome,lista_pares):
    dic = {x : lista_pares for x in nome}
    print(dic)

dicionario(nome,lista_pares)