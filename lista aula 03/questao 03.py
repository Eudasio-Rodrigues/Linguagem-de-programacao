# Escreva um programa que pergunte a distância que um passageiro deseja
# percorrer em km. Calcule o preço da passagem, cobrando R$ 0.50 por km
# para viagens de até 200 km, e R$ 0.45 para viagens mais longas.

distancia= int(input("Digite a distancia da sua viagem. Km: "))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print(f"O valor da sua passagem é de R${passagem}")