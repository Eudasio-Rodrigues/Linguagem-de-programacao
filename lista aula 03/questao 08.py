def maior_numero(numeros):
    print(f"O maior numero da lista é {max(numeros)}")
    
numeros = [int(input("Número: ")) for i in range(5)]
maior_numero(numeros)
