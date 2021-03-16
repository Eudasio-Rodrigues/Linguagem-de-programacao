#Encapsule o código da questão anterior em uma função, que recebe a lista criada
#e a letra de uma operação. A função deve retornar o resultado da operação
#representada por esta letra de acordo com o enunciado da questão anterior.
import os
def operacao(lista,letra):
    if letra == "a" or letra == "A":
        print(f"Os dez primeiros números da lista são: {lista[0:10]}\n")
    elif letra == "b" or letra == "B":
        print(f"Os dez últimos números da lista são: {lista[31:41]}\n")
    elif letra == "c" or letra == "C":
        print(f"Os cinco itens do meio da lista são: {lista[18:23]}\n")
    elif letra =="d" or letra == "D":
        lista.reverse()
        print(f"lista reversa: {lista}\n")
    elif letra == "e" or letra == "E":
        print(f"primeiro indice {lista[0]} ,ultimo indice {lista[-1]}\n")
    elif letra == "f" or letra == "F":
        lista = [item**2 for item in range(0,41)]
        print(f"Itens elevados ao quadrado: {lista}\n")
    elif letra == "g" or letra == "G":
        lista = [numero for numero in range(0,41) if numero % 2 == 0]
        print(f"Lista dos pares: {lista}")
    else:
        print("letra invalida")

letra = input("Digite uma letra\n")
os.system('clear') 
lista = []

for i in range(0,41):
    lista.append(i)

operacao(lista,letra)