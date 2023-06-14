import json
# Na estrutura proposta, a classe principal é a Turma, que representa uma turma específica e possui um professor e uma lista de alunos. Além disso, temos outras entidades relacionadas, como Aluno, Professor e Coordenador.

# A relação entre as classes é a seguinte:

#    A classe Turma depende da classe Professor para ter um professor associado a ela.
#    A classe Turma também depende da classe Aluno para ter uma lista de alunos matriculados.
#    A classe Professor é independente das outras classes e não depende delas.
#    A classe Coordenador é uma entidade preexistente no sistema e não depende das outras classes.

# Resumindo, a classe Turma depende da classe Professor e da classe Aluno, enquanto as classes Professor, Aluno e Coordenador são independentes entre si.


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


class Professor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.professores=[]

class Coordenador:
    def __init__(self):
        self.__coordenador = "Alisson"
        self.turmas = []

    def criar_turma(self):
        disciplina = input("Digite o nome da disciplina: ")
        professor = self.escolher_professor()
        alunos = self.escolher_alunos()
        turma = Turma(disciplina, professor)
        for aluno in alunos:
            turma.adicionar_aluno(aluno)
        self.turmas.append(turma)

    


class Turma(Professor, Aluno):
    def __init__(self, disciplina, professor):
        self.disciplina = disciplina
        self.professor = professor
        self.alunos= []
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def remover_aluno(self, aluno):
        self.aluno.remove(aluno)
    
    def listar_alunos(self):
        for aluno in self.alunos:
            print(f"Nome: {aluno.nome}, Matrícula: {aluno.matricula}")
    
    def visualizar_turma(self):
        print(f"Disciplina:  {self.disciplina}")
        print(f"Professor:  {self.professor.nome}")
        print("Alunos:")
        self.listar_alunos()
    