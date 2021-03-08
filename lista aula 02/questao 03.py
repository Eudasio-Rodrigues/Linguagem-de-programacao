#Crie uma função que retorne o resto da divisão do resultado da função da questão anterior por 2
n1 = int(input("Digite primeiro numero:\n"))
n2 = int(input("Digite segundo numero:\n"))

def calculo(n1, n2):
    return  (2 * n1) * (3 * n2)

x=calculo(n1,n2)

def resto(x):
    return x % 2

print(f"O resultado é: {calculo(n1, n2)}")
print(f"O resto da divisao de {calculo(n1, n2)} por 2 é {resto(x)}")