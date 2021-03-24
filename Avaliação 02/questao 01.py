# Crie um arquivo que contenha todos os números pares de 2 a 100:
# Criação do arquivo
with open("numeros.txt", "w") as numeros:
    for i in range(2, 101):
        if i % 2 == 0:
            numeros.write(f"{i}\n")