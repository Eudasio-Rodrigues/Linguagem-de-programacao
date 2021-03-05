from  time import sleep 
import os
x = 10
while x > -1:
    for contagem in range(2):
        sleep(1)
        print(x)
        x = x-1
        
os.system('clear')  
print('Fogo')
    