def aumento_salarial(salario):

    if salario > 1250:
        aumento = salario + (0.10 * salario)
        print("Seu salario com reajuste de 10% vai para {:.2f}".format(aumento))
    
    else:
        aumento = salario + (0.15 *salario)
        print("Seu salario com reajuste de 15% vai para {:.2f}".format(aumento))

salario= float(input("Diga qual seu salario atual: R$ "))
aumento_salarial(salario)
