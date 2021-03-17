#Escreva uma função que crie listas automaticamente dentro de um intervalo de
# dois números passados como parâmetros



def cria_lista(n1,n2):
    lista=[]
    for i in range(n1,n2):
        lista.append(i)
    print(lista)

n1= int(input("Digite um numero\n"))
n2=int(input("Digite outro numero\n"))

cria_lista(n1,n2)