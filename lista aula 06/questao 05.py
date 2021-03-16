#Escreva um programa que gere automaticamente uma lista com 40 inteiros e
#faça o que se pede a seguir:
#a- imprima o primeiro quarto da lista
#b -imprima o último quarto da lista
#c -imprima os 5 itens do meio da lista
#d -imprima a lista reversa
#e - Imprima o primeiro e o último item da lista
#Utilize list comprehension para :
#f - Gerar uma lista com o quadrado de cada item da lista original
#g - Gerar uma lista com apenas itens pares da lista original

lista = []
for i in range(0,41):
    lista.append(i)
print(f"Lista completa {lista}\n")
print(f"a = {lista[0:10]}\n")
print(f"b = {lista[31:41]}\n")
print(f"c = {lista[18:23]}\n")
lista.reverse()
print(f"d = {lista}\n")
print(f"primeiro indice {lista[-1]} ,ultimo indice {lista[0]}\n")
lista = [item**2 for item in range(0,41)]
print(f"{lista}\n")
lista = [numero for numero in range(0,41) if numero % 2 == 0]
print(lista)