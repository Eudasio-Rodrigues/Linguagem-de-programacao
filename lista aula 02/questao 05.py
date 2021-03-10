#Escreva uma função que receba como argumento a quantidade de Km percorridos por um carro
#alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. 
#A função deve retornar o preço a pagar sabendo que o carro
#custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_rodado=int(input("Quantos km foram percorridos: "))
aluguel_dias=int(input("Quantos dias o carros ficou alugado: "))

def valor_para_pagar(km_rodado, aluguel):
    preco_a_pagar = (aluguel_dias * 60) + (km_rodado * 0.15)
    print(f"Você irá pagar R${preco_a_pagar}")

valor_para_pagar(km_rodado, aluguel_dias)