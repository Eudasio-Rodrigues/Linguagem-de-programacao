#Escreva uma função que simule o funcionamento de um radar eletrônico. 
#Essa função deve receber a velocidade do carro de um usuário. 
#Caso ultrapasse 80 Km/h, exiba uma mensagem dizendo que o usuário foi multado. 
#Nesse caso, exiba o valor da multa, cobrando R$ 90 reais pela infração + R$ 5 reais por km acima de 80 km/h

def radar_eletronico(velocidade):
    km_rodado=5 #valor da ,ulta por km rodado

    if velocidade > 80:#condiçao pra checar se o motorista está dentro do limite
        print(f"Você foi multado por excesso de velocidade")
        multa=90 + (velocidade-80) * km_rodado
        print(f"Sua multa é de R${multa}")
    else:
        print("Você estava dentro do limite")

velocidade=int(input("Digite a velocidade do carro-> "))
radar_eletronico(velocidade)
