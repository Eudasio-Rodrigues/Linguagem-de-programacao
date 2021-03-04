num1=int(input("Digite primeiro numero: "))
num2=int(input("Digite segundo numero: "))
print("adição=(+), subtração=(-),multiplicação=(*), divisão=(/)")
op=input("digite operação")

if op=="+":
    adição=num1+num2
    print(adição)
elif op =="-":
        subtração=num1-num2
        print(subtração)
elif op =="*":
            multiplicação=num1*num2
            print(multiplicação)
else:
                divisao=num1/num2
                print(divisao)