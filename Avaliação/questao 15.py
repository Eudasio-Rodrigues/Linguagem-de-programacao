# 15-​Imprimia as seguintes sequências utilizando `for` e o método `range()`:
#ímpares de 1000 a 43
#pares de 2 a 100
lista_impares =[]
lista_par = []

for i in range(43,1000):
    if i % 2 != 0:
        lista_impares.append(i)
for i in range(2,101):
    if i % 2 == 0:
        lista_par.append(i)

lista_impares.reverse()
print(f"LISTA DE NUMEROS IMPARES\n{lista_impares}\n\n")
print(f"LISTA DE NUMEROS PARES\n{lista_par}")