#Escreva uma função para calcular a redução do tempo de vida de um fumante. 
#Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, 
# a função deverá retornar quantos dias de vida um fumante perderá. Exiba o total em dias.

qtd_cigarros = int(input("Quantos cigarros voce fuma por dia\n"))
qtd_anos_fuma = int(input("Ha quantos anos voce fuma\n"))

def reducao_vida(qtd_cigarros, qtd_anos_fuma):
    dias_fumando = qtd_anos_fuma * 365
    cigarros_fumados = qtd_cigarros * dias_fumando
    minutos_perdidos_vida = cigarros_fumados * 10
    minutos_dia = 24*60
    dias_perdidos_de_vida = minutos_perdidos_vida / minutos_dia

    print(f"Voce perdeu {dias_perdidos_de_vida:.1f} dias da sua vida fumandos")

reducao_vida(qtd_cigarros,qtd_anos_fuma)