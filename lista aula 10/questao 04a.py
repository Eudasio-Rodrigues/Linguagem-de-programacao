class Conta:
    # contrutor
    def __init__(self, numero, titular, saldo, agencia=4391):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.agencia = agencia

    def mostrar_saldo(self):
        print(f'Seu saldo é R$ {self.saldo} Reais')

    def depositar(self, valorD):
        self.saldo += valorD
    def sacar(self, valorS):
        if self.saldo <= 0:
            print("Não há saldo")
        else:
            self.saldo -= valorS

    def transferir(self, contaDestino, valorT):
        if self.saldo >= valorT:
            self.saldo -= valorT
            contaDestino.saldo += valorT
        else:
            print("Não tem saldo")


c1 = Conta(123, "Rafael", 100)
c2 = Conta(124, "Cunhado", 0)

c1.mostrar_saldo()
c1.depositar(50)
c1.sacar(40)
c1.transferir(c2, 112)
c1.mostrar_saldo()
c2.mostrar_saldo()