#Utilizando o dicionário criado na questão anterior faça: Uma função que retorne apenas 
# os valores pares do dicionario da questão anterior Uma função que retorne apenas as chaves
#vogais do dicionário da questão anterior
nome='EUdAsIO'

def dicionario(nome):
    dic = {x : [x for x in range(10) if x %2 == 0 ] for x in nome}
    print(dic)
    print("\n")
dicionario(nome)

lista_vogais=['A','E','I','O','U']
def vogais(nome,lista_vogais):
    for i in nome:
        if i.upper() in lista_vogais:
            print(i, end =" -")
vogais(nome,lista_vogais)
print('\n')

def numeros(nome):
    dic = {x : [x for x in range(7) ] for x in nome} 
    for k in dic.values(): # Percorre apenas os valores
      for i in k:  # Percorre as listas (valores)
        if i % 2 == 0:
          print(i, end = "- ")

numeros(nome)