#3 -​ Escreva uma função para calcular a redução do tempo de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que um fumante perde 10 minutos de vida a cada cigarro, a função
# deverá retornar quantos dias de vida um fumante perde. Exiba o total em segundos.

qtd_cigarros = int(input("Quantos cigarros voce fuma por dia\n"))
qtd_anos_fumando = int(input("Ha quantos anos voce fuma\n"))

def reducao_vida(qtd_cigarros, qtd_anos_fuma):
    dias_fumando = qtd_anos_fumando * 365
    cigarros_fumados = qtd_cigarros * dias_fumando
    minutos_perdidos_vida = cigarros_fumados * 10
    segundos_dia = 24*60*60
    dias_perdidos_de_vida = minutos_perdidos_vida * segundos_dia
    print(f"Voce perdeu {dias_perdidos_de_vida:.1f} segundos da sua vida fumandos")

reducao_vida(qtd_cigarros,qtd_anos_fumando)