#Escreva uma função que receba a idade do usuário e
#indique se ele pode ou não encher a cara de cachaça.

idade= int(input("Qual sua idade?\n"))

def encher_a_cara(idade):
    if idade >=18:
        print("Voce pode beber até cair")
    else:
        print("Vai estudar que é melhor.")

encher_a_cara(idade)
