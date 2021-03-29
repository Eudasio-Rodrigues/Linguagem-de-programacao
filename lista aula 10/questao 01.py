#Implemente a classe Funcionário com os seguintes atributos(matrícula, setor, valor_hora,
# número de faltas), construa métodos que você acha útil para essa classe.

class Funcionário:
    def __init__(self, matricula, setor, valor_hora, numero_de_faltas, horas_trabalhadas):
        self.matricula = matricula
        self.setor = setor
        self.valor_hora = valor_hora
        self.numero_de_faltas = numero_de_faltas
        self.horas_trabalhadas = horas_trabalhadas

    def mostrar_dados(self):
        print(f"""matricula: {self.matricula}
        setor: {self.setor}
        valor da hora: R${self.valor_hora}
        numero de faltas: {self.numero_de_faltas}""")
    
    def salario_mes(self):
        salario = self.horas_trabalhadas * self.valor_hora
        print(f"salario R${salario}")

    def desconto_salario(self):
        salario = self.horas_trabalhadas * self.valor_hora
        if self.numero_de_faltas >= 10:
            desconto = salario * 0.05
            salario_final = salario - desconto
            print(f"Voce faltou mais de 10 vezes e seu salario terá desconto.")
            print(f"Seu salário esse mes é de: {salario_final}")
        else:
            print(salario)

    def demissao(self):
        if self.numero_de_faltas >=30:
            print(f"Você faltou muitas vezes, está demitido")
        else:
            print(f"Você é um funcionario exemplar,continue assim.")
    

funcionario01 = Funcionário(1491558,'limpeza',10, 30, 200)
funcionario01.mostrar_dados()
funcionario01.salario_mes()
funcionario01.desconto_salario()
funcionario01.demissao()