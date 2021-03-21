#Escreva uma função que receba uma lista de vários inteiros e retorne um único
#inteiro composto por todos os itens da lista informada.
a=[1,2,3,4]
def f(l):
    if not l: return 0
    return l[-1] + f(l[:-1]) * 10

print(f(a))