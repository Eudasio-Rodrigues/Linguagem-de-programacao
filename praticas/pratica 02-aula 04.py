'''def maior_numero(numeros):
    print(f"O maior numero da lista é {max(numeros)}")'''

#transformação da funçao acima em funçao lambda pra achar o maior numero
maior_numero= lambda numeros:print(max(numeros))
numeros = [int(input("Número: ")) for i in range(5)]
maior_numero(numeros)

