#Escreva uma função para aprovar o empréstimo bancário para compra de uma casa.
# Essa função deve receber o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
#O valor da prestação mensal não pode ser superior a 30% do salário. 
#Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

def emprestimo(valor_casa, salario, quantidade_anos):
    meses = quantidade_anos * 12#transformaçao dos anos em meses
    prestacao_casa = valor_casa / meses#divisao do valor da casa pelos meses a pagar 
    prestacao = salario * 0.30#verificaçao se a prestaçao é maior do que 30% do salario

    if prestacao_casa > prestacao:
        print("Voce não pode comprar a casa")
    
    else:
        
        print(f"Voce irá pagar sua casa em {meses} prestações de R${prestacao_casa:.2f}")

valor_casa=float(input("Qual o valor da casa:R$ "))
salario=float(input("Digite seu salário:R$ "))
quantidade_anos=int(input("Quantidade de anos para pagar a casa: "))
emprestimo(valor_casa, salario, quantidade_anos)