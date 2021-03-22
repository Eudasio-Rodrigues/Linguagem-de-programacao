#Faça uma função que retorne uma das três operações básicas entre sets:
#A função deve receber dois conjuntos que terão itens adicionados manualmente pelo usuário
#A operação que será retornada também será escolhida pelo usuário

lista1 = []
lista2 = []

lista1 = [(input("Digite os 5 itens da lista 1\n")) for c in range(3)]
lista2 = [(input("Digite os 5 itens da lista 2\n")) for c in range(3)]

set1 = set(lista1)
set2 = set(lista2)

print("d = Diferença , u = União ou i = Intesecção")
op = str(input("digite a operação do set-->\n"))

def opcao(set1, set2, op):
    if op == "d":
        print(set1  - set2)
    elif op == "u":
        print(set1  | set2)
    elif op == "i":
        print(set1.intersection(set2))
    else:
        return "invalido, informe d = Diferença , u = União ou i = Intesecção"

opcao(set1, set2, op)
