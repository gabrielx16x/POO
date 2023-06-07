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
        self.__nome = nome
        self.__matricula = matricula
        self.alunos= []


class Professor:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.professores=[]

class Coordenador:
    def __init__(self):
        self.__coordenador = "Alisson"
    


class Turma(Professor, Aluno):
    def criar_turma(self, aluno, professor):
        self.turma = []
        self.append(aluno,professor)
        
