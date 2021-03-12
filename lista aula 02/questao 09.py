#Crie uma função que receba duas strings e retorne True se o número de elementos de uma for igual
#ao da outra, e retorne False caso contrário.Pesquise pelo método len() na documentação do Python.

string1=input("Digite uma palavra\n")
string2=input("Digite outra palavra\n")

def tamanho_string(string1, string2):
    if len(string1) == len(string2):
        return True
    else:
        return False

print(tamanho_string(string1,string2))
tamanho_string(string1,string2)