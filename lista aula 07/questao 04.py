#Utilizando dic conprehension e list comprehension construa uma função que gere o seguinte dicionário: 
#O dicionario deve ter como chave as letras de um nome inserido como argumento e 
# como valor uma lista de pares dentro de um range, passado também como argumento

nome='eudasio'
def dicionario(nome):
    dic = {x : [x for x in range(10) if x %2 == 0 ] for x in nome}
    print(dic)

dicionario(nome)