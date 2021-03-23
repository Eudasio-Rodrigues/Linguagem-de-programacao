#Percorra as listas anteriores e adapte alguma questão para que ao invés de imprimir 
#a solução no terminal ela guarde esse dado em um arquivo
nome = "marcelo"


def dicionario(nome):
    dicionario = open("dicionario.txt", "w")
    dic = {x: [x for x in range(10) if x % 2 == 0] for x in nome}
    dicionario.write(f"{dic}\n")
    dicionario.close()


dicionario(nome)