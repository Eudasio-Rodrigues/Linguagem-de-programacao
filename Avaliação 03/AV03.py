class Secretaria:
    def __init__(self,notas=[]):
        self.notas = notas
        self.n1=int(input("nota 1: "))
        self.n2=int(input("nota 2: "))
        self.n3=int(input("nota 3: "))

    def adicionar_notas (self):
        self.notas.append(self.n1)
        self.notas.append(self.n2)
        self.notas.append(self.n3)
    
    def visualizar_notas(self):
        print(f"""
                Nota1: {self.notas[0]}
                Nota2: {self.notas[1]}
                Nota3: {self.notas[2]}
         
         """)
class Alunos:
    def __init__(self):
       
        self.matricula_aluno = int(input("Digite sua matricula: "))
        self.nome_aluno = input("Digite seu nome: ")
        self.dia_da_semana= input("Que dia é hoje: ")

    def assistir_aula(self):
        if self.dia_da_semana == "sabado" or self.dia_da_semana == "domingo":
            print("Oba! Hoje vou assistir desenho")
        else:
            print("ah nao, eu tenho mesmo que ir pra escola mãe?")

    def mostrar_dados(self):
            print(f"nome:{self.nome_aluno}\nmatricula:{self.matricula_aluno}")    
    
class Professores():
    def __init__(self):
        self.dia_trabalhados= int(input("Dias trabalhados: "))
        self.dia_letivos = int(input("Dias letivos: "))

    def aulas(self):
        if self.dia_trabalhados < self.dia_letivos:
            print("Preciso planejar as aulas dessa semana")
        else:
            print("Finalmente férias")
        
aluno = Alunos()
aluno.assistir_aula()
aluno.mostrar_dados()
sec=Secretaria()
sec.adicionar_notas()
prof=Professores()
prof.aulas()

