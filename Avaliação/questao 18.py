#18-​ Em campeonato de futebol por pontos corridos, as pontuações funcionam da
#seguinte forma: 0 pontos por derrota, 1 ponto por empate e 3 pontos por vitória.
#Construa uma função que receba a quantidade de vitórias, derrotas e empates de
#um time e retorne a sua pontuação total ao fim do campeonato
derrota = int(input("Numeros de derrotas:\n"))
vitoria =int(input("Numeros de vitoria:\n"))
empate = int(input("Numeros de empate:\n"))

def resultado(derrota,vitoria,empate):
    pontuaçao_final = (derrota* 0) + (empate * 1) + (vitoria * 3)
    print(pontuaçao_final)

resultado(derrota,vitoria,empate)