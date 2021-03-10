input = input('Escreva qualquer coisa: ')
input = input.lower()
output = []
def troca(output):
    for caracteres in input:
        numero = ord(caracteres) - 96
        output.append(numero)
        
troca(output)
print (output)

