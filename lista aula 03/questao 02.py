#Faça uma função que receba como argumento o salário de um funcionário e 
#calcule o valor do aumento com base nos dados abaixo.
#Para salários superiores a R$ 1.250,00 Reais, calcule um aumento de 10%
#Para os inferiores ou iguais, 15% de aumento.

Para salários superiores a R$ 1.250,00 Reais, calcule um aumento de 10%
Para os inferiores ou iguais, 15% de aumento.
def aumento_salarial(salario):

    if salario > 1250:
        aumento = salario + (0.10 * salario)
        print(f"Seu salario com reajuste de 10% vai para {aumento}")
    
    else:
        aumento = salario + (0.15 *salario)
        print(f"Seu salario com reajuste de 15% vai para {aumento}")

salario= float(input("Diga qual seu salario atual: R$ "))
aumento_salarial(salario)
