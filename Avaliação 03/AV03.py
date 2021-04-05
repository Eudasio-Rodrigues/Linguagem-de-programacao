#Eudasio
#Estagio na secretria da escola Pedro Jaime
class Secretaria:
    def __init__(self,notas=[]):
        self.notas = notas
        self.n1=int(input("nota 1: "))
        self.n2=int(input("nota 2: "))
        self.n3=int(input("nota 3: "))
       
#metodo da secretaria para adicionar as notas dos alunos no sistema
    def adicionar_notas (self):
        self.notas.append(self.n1)
        self.notas.append(self.n2)
        self.notas.append(self.n3)
    
class Alunos():
    def __init__(self):
#entrada de dados do aluno
        self.matricula_aluno = int(input("Digite sua matricula: "))
        self.nome_aluno = input("Digite seu nome: ")
        self.dia_da_semana= input("Que dia é hoje: ")
#verificaçao sobre o dia da semana para saber se tem aula ou é final de semana
    def assistir_aula(self):
        if self.dia_da_semana == "sabado" or self.dia_da_semana == "domingo":
            print("Oba! Hoje vou assistir desenho")
        else:
            print("ah nao, eu tenho mesmo que ir pra escola mãe?")
#mostra dados do aluno
    def mostrar_dados(self):
            print(f"nome:{self.nome_aluno}\nmatricula:{self.matricula_aluno}")   
class Professores():
    def __init__(self):
#pedindo dados para saber se o prfessor ja cumpriu carga horaria
        self.dia_trabalhados= int(input("Dias trabalhados: "))
        self.dia_letivos = 200
#metodo que verifica se o professor ainda precisa dar aula ou está de ferias
    def aulas(self):
        if self.dia_trabalhados < self.dia_letivos:
            print("Preciso planejar as aulas dessa semana")
        else:
            print("Finalmente férias")

class Biblioteca:
    def __init__(self):
        self.livro=input("Qual livro voce quer pegar: ")
    
    def emprestar(self):
        self.lista=['HP a pedra filosofal','HP e a camara secreta']
        for self.livro in self.lista:
            if self.livro not in self.lista:
                print("o livro nao está disponivel")
            else:
                print("Aqui está ele. Voce tem 7 dias para devolver")
'''aluno = Alunos()
aluno.assistir_aula()
aluno.mostrar_dados()
sec=Secretaria()
sec.adicionar_notas()
prof=Professores()
prof.aulas()'''
biblioteca=Biblioteca()
biblioteca.emprestar()