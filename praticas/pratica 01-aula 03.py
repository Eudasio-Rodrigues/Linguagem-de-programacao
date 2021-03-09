def desconto(preco, categoria):
    
    if categoria == 1:
        return preco - 0.05 * preco

    elif categoria == 2:
        return preco - 0.07 * preco

    elif categoria == 3:
        return preco - 0.10 * preco
    
    elif categoria == 4:
        return preco - 0.15 * preco
    
    else :
        return preco - 0.20 * preco
    
list=[1,2,3,4,5]#lista contendo as categorias que podem ser escolhidas,ela serve 
                #para que usuario nao digite qualquer numero e cause erros
preco=float(input("Digite o preço do produto-->R$ "))
categoria=' '
while categoria not in list:#condição que obriga o usuario a digitar o numero de 1 a 5 apenas
    categoria=int(input("Digite a categoria do produto entre 1 e 5--> "))
    
desconto(preco,categoria)#passagem dos valores para a funçao
print("O valor do produto com desconto é de R${}".format(desconto(preco,categoria)))