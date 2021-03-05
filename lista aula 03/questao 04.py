def emprestimo(valor_casa, salario, quantidade_anos):
    meses = quantidade_anos * 12#transformaçao dos anos em meses
    prestacao_casa = valor_casa / meses#divisao do valor da casa pelos meses a pagar 
    prestacao = salario * 0.30#verificaçao se a prestaçao é maior do que 30% do salario

    if prestacao_casa > prestacao:
        print("Voce não pode comprar a casa")
    
    else:
        
        print("Voce irá pagar sua casa em {} prestações de R${:.2f}".format(meses,prestacao_casa))

valor_casa=float(input("Qual o valor da casa:R$ "))
salario=float(input("Digite seu salário:R$ "))
quantidade_anos=int(input("Quantidade de anos para pagar a casa: "))
emprestimo(valor_casa, salario, quantidade_anos)