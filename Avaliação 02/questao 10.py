#Escreva um programa que gere automaticamente uma lista com 100 inteiros e faça o que se pede a seguir:
#Uma lista com os números pares
#uma lista com os números múltiplos de 5

lista = [x for x in range(1,101)]

lista_pares  =[]
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
print(f"{lista_pares}\n")

lista_mult = []
for i in lista:
    if i % 5 == 0:
        lista_mult.append(i)
print(lista_mult)