#Gere as seguintes listas utilizando for e o metodo range():

#Uma lista de ímpares de 10 a 120
#Uma lista pares de 2 a 1000
#Uma lista de multiplos de 2 em um intervalo decrescente de 100 até 40
#Uma lista de primos de 44 até 99
#OBS: Pesquise pelo método append() na documentação

lista_impares=[]
lista_pares=[]
lista_multiplos = []
lista_primos= []

#lista de numeros impares
for i in range(10,120):
    if i % 2 != 0:
        lista_impares.append(i)
print(f"LISTA DOS NUMEROS ÍMPARES: {lista_impares}\n\n")

#lista de numeros pares
for i in range(2,1001):
    if i % 2 == 0:
        lista_pares.append(i)
print(f"LISTA DOS NUMEROS PARES: {lista_pares}\n\n")

#lista de numeros multiplos de 2
for i in range(40,101):
    if i % 2 == 0:
        
        lista_multiplos.append(i)
lista_multiplos.reverse()
print(f"LISTA DOS MULTIPLOS DE 2 DECRESCENTE: {lista_multiplos}\n\n")

#lista de primos de 44 ate 99
lista_primos = []

for x in range(44,100):
    cont=0

    for y in range(1, x+1):
        if x % y == 0:
            cont += 1
    if cont <= 2:
            lista_primos.append(x)

print(F"LISTA DOS PRIMOS DE 44 ATÉ 99: {lista_primos}")