def nome_usuario(nome):
    return nome

def idade_usuario(idade):
    return idade

def estado_civil(estadocivil):
    return estadocivil

def genero_usuario(genero):
    return genero

nome = input("Seu nome: ")
idade = int(input("Sua idade: "))
estadocivil = input("Seu estado civil: ")
genero = input("Seu genero: ")

print("\n\n\n")

print("Seu nome é ",nome_usuario(nome))
print("Sua idade é ",idade_usuario(idade))
print("Você é ", estado_civil(estadocivil))
print("Voce é do genero ", genero_usuario(genero))