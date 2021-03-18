#Escreva uma função que recebe uma lista de inteiros e que retorne a mesma
# lista , mas que no lugar de cada inteiro par deve estar escrito a palavra ‘Par’.

lista = [x for x in range(1,21)]


def par(lista,par):
   lista[1]=par
   lista[3]=par
   lista[5]=par
   lista[7]=par
   lista[9]=par
   lista[11]=par
   lista[13]=par
   lista[15]=par
   lista[17]=par
   lista[19]=par

   print(lista)

par(lista,'par')