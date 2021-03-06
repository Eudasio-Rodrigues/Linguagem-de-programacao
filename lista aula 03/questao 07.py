loop = True
lista = []

while(loop):
    numero = int(input("Digite um numero diferente de zero, ou zero para encerrar\n"))
    if numero != 0:
        lista.append(numero)
    else:
        loop = False

print (f"A quantidade de valores inseridos é de {len(lista)}")
print (f"A soma dos valores inseridos é de {sum(lista)}")
print (f"A média dos valores inseridos é de {round(sum(lista) / len(lista))}")