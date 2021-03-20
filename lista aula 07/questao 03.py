#Escreva uma função que receba um dicionário composto por 2 chaves(login e senha),
#essas chaves devem possuir seus respectivos valores. A função deve receber além
#do dicionário, dois possiveis valores para as duas chaves, dentro da função
#deve ser feita uma verificação que irá retornar "Acesso concedido" se o valor 
#de login e senha do dicionário forem iguais aos que foram passados no chamado
#da função. Para ficar mais interessante,receba o login e senha do usuário através do input.

acesso_usuario = {'login':'eudasio',
                  'senha': 'n4o3d45u4c0nt4'}

login = input("Digite seu usuario\n")
senha = input("Digite sua senha\n")

def checar_acesso(acesso_usuario,login,senha):
    if login == 'eudasio' and senha == 'n4o3d45u4c0nt4':
        print("Acesso concedido")
    else:
        print("Acesso negado")


checar_acesso(acesso_usuario,login, senha)