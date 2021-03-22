#Escreva uma função que faça a verificação de existência de uma chave 
#dentro de um dicionário. Caso a chave exista a função deve retornar o 
# valor da chave, caso ela não exista, a função deve adicioná-la e 
# retornar o dicionário.

dados_pessoais={'nome':"Eudasio",
                "idade": 27,
                "cidade":'Mombaça',
                "estado_civil":'solteiro'
                }

chave=(input("Qual chave voce quer procurar\n"))

def verifica_chave(dados_pessoais, chave):
   
    if chave in dados_pessoais:
        print(dados_pessoais[chave])
    else:
        print("Chave não econtrada")
        dados_pessoais[chave]=" chave adicionada"
        print(dados_pessoais)


verifica_chave(dados_pessoais,chave)