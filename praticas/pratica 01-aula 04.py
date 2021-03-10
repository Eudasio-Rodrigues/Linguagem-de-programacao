vendas=float(input("Total de vendas do funcionario\n"))

salario=1100
def bonus_salario(vendas, nome='Eudasio'): 
    global salario
    if vendas > 550.00:
        salario +=  550
        print(f"{nome} você irá receber {salario}")
    else:
        print(f"{nome} você irá receber {salario}")

bonus_salario(vendas)