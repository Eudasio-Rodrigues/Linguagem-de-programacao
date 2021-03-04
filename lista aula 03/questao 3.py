distancia= int(input("Digite a distancia da sua viagem. Km: "))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print("O valor da sua passagem é de R${}".format(passagem))