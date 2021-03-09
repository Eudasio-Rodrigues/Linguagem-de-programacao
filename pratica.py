n1= int(input("lado 1: "))
n2= int(input("lado 2: "))
n3= int(input("lado 3: "))

'''def perimetro(n1,n2,n3=10):
    return n1+n2+n3
'''
perimetro = lambda n1,n2,n3: n1+n2+n3

print(perimetro(n1,n2,n3))

'''def imprimir_perimetro(perimetro):
    print(perimetro)

imprimir_perimetro(perimetro(n1,n2))
'''