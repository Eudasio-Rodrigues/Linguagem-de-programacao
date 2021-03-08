#Escreva uma função que receba dois números como argumento e
#retorne o produto do dobro do primeiro pelo triplo do segundo

def calculo(num1, num2):
    return (2 * num1) * (3 * num2)

n1 = int(input("Digite primeiro numero:\n"))
n2 = int(input("Digite segundo numero:\n"))
calculo(n1, n2)
print(f"O resultado é: {calculo(n1, n2)}")