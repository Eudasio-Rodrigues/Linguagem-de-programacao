#Escreva três funções que gerem automaticamente dicionários com dic comprehensions.
#Em seguida utilize essas funções como argumentos de outra função que irá recebê-las e 
#retornar um único dicionário

def dic1(dicionario01):
    dicionario01 = {x:x for x in range(0,11)}
    return dicionario01

def dic02(dicionario02):
    dicionario02 ={x:x for x in range(11,21)}
    return dicionario02

def dic03(dicionario03):
    dicionario03 ={x:x for x in range(21,31)}
    return dicionario03
    
def dic_unidas(dic1, dic02, dic03):
    dic1.update(dic02)
    dic02.update(dic03)
    print(dic1)

dic_unidas(dic1('dicionario01'), dic02('dicionário02'), dic03('dicionário03'))