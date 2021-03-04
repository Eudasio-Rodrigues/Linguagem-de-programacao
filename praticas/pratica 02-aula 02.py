def match(eu, pessoa02):
    solteiro='s'
    casado='c'
    if (eu == solteiro) and (pessoa02 == solteiro):
        return print("Bora")
    else:
        return print("Deixa quieto")


print("s=solteiro e c=casado")
eu = input("Meu estado civil-->") 
pessoa02=input("Diga o seu estado civil--> ")

match(eu,pessoa02)