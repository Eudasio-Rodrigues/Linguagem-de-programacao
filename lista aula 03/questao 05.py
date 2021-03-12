#Faça um programa para escrever a contagem regressiva do lançamento de um foguete. 
#O programa deve imprimir 10, 9, 8..., 1, 0 e "Fogo!", na tela.

from  time import sleep 
import os
x = 10
while x >= 0:
    for contagem in range(1):
        sleep(2)
        print(x)
        x = x-1
        
os.system('clear')  
print('Fogo')
