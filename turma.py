import sqlite3
from tkinter import * 
import tkinter as tk
try:
    con = sqlite3.connect('gestao_turmas.db')
    print("Conexão com o banco de dados realizado com sucesso")
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS Alunos(id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT, 
                    matricula TEXT
        )""")
        
        print("Tabela Alunos criada com sucesso.")

except sqlite3.Error as e:
    print("Erro ao criar a tabela Alunos:", e)


try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS Professores (
                    id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT, 
                    matricula TEXT
                  
        )""")
        print("Tabela Professores criada com sucesso.")

except sqlite3.Error as e:
    print("Erro ao criar a tabela Professores:", e)
    
try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS Turmas ( 
                    id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
                    disciplina TEXT, 
                    id_professor INTEGER,
                    FOREIGN KEY (id_professor) REFERENCES Professores (id_professor)
                  
        )""")
        print("Tabela Turmas criada com sucesso.")

except sqlite3.Error as e:
    print("Erro ao criar a tabela Turmas:", e)
    

try:
    with con:
        cur = con.cursor()
        cur.execute(""" CREATE TABLE IF NOT EXISTS Turmas_Alunos ( 
                    id_turma INTEGER,
                    id_aluno INTEGER,
                    FOREIGN KEY (id_turma) REFERENCES Turmas (id_turma),
                    FOREIGN KEY (id_aluno) REFERENCES Alunos (id_aluno),
                    PRIMARY KEY (id_turma, id_aluno)
                  
        )""")
        print("Tabela Turmas_Alunos criada com sucesso.")

except sqlite3.Error as e:
    print("Erro ao criar a tabela Turmas_Alunos:", e)

    
    
class Aluno:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula

        
class Professor:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        
    @property
    def nome(self):
        return self._nome

    @property
    def matricula(self):
        return self._matricula


class Turma:
    def __init__(self, disciplina, professor):
        self._disciplina = disciplina
        self._professor = professor
        self._alunos = []
    
    def adicionar_aluno(self, nome, matricula):
        aluno = Aluno(nome, matricula)
        cur.execute("INSERT INTO Alunos VALUES (?, ?)", (nome, matricula))
        con.commit()
        self._alunos.append(aluno)
        
    def remover_aluno(self, aluno_id):
        self._alunos = [aluno for aluno in self._alunos if aluno.id_aluno != aluno_id]
        cur.execute("DELETE FROM Turmas_Alunos WHERE id_turma = ? AND id_aluno = ?", (self.id_turma, aluno_id))
        con.commit()
        
    def ver_alunos(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT nome, matricula FROM Alunos INNER JOIN Turmas_Alunos ON Alunos.id_aluno = Turmas_Alunos.id_aluno WHERE Turmas_Alunos.id_turma = ?", (self.id_turma,))
                alunos = cur.fetchall()

                if alunos:
                    for i, aluno in enumerate(alunos):
                        nome = aluno[0]
                        matricula = aluno[1]
                        print(f"{i+1} - Nome: {nome} Matrícula: {matricula}")
                else:
                    print("Não há alunos matriculados nesta turma.")

        except sqlite3.Error as e:
            print("Erro ao obter os alunos da turma:", e)

class Coordenador:
    def criar_turma(self, disciplina, professor, alunos):
        try:
            with con:
                cur = con.cursor()
                # Inserir professor na tabela Professores
                cur.execute("INSERT INTO Professores (nome, matricula) VALUES (?, ?)",
                            (professor.nome, professor.matricula))
                professor_id = cur.lastrowid

                # Inserir turma na tabela Turmas
                cur.execute("INSERT INTO Turmas (disciplina, id_professor) VALUES (?, ?)",
                            (disciplina, professor_id))
                turma_id = cur.lastrowid

                # Inserir alunos na tabela Alunos e relacionar com a turma na tabela Turmas_Alunos
                for aluno in alunos:
                    cur.execute("INSERT INTO Alunos (nome, matricula) VALUES (?, ?)",
                                (aluno.nome, aluno.matricula))
                    aluno_id = cur.lastrowid
                    cur.execute("INSERT INTO Turmas_Alunos (id_turma, id_aluno) VALUES (?, ?)",
                                (turma_id, aluno_id))

                print("Turma criada com sucesso!")

        except sqlite3.Error as e:
            print("Erro ao criar a turma:", e)
    def editar_turma(self, turma_id, novo_professor=None, alunos_adicionar=None, alunos_remover=None):
        try:
            with con:
                cur = con.cursor()

                # Atualizar professor da turma
                if novo_professor:
                    cur.execute("UPDATE Turmas SET id_professor = ? WHERE id_turma = ?",
                                (novo_professor.id, turma_id))

                # Adicionar novos alunos à turma
                if alunos_adicionar:
                    for aluno in alunos_adicionar:
                        cur.execute("INSERT INTO Turmas_Alunos (id_turma, id_aluno) VALUES (?, ?)",
                                    (turma_id, aluno.id))

                # Remover alunos da turma
                if alunos_remover:
                    for aluno in alunos_remover:
                        cur.execute("DELETE FROM Turmas_Alunos WHERE id_turma = ? AND id_aluno = ?",
                                    (turma_id, aluno.id))

                print("Turma atualizada com sucesso!")

        except sqlite3.Error as e:
            print("Erro ao editar a turma:", e)
    
    
    
    
    def cadastrar_professor(self, nome, matricula):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Professores (nome, matricula) VALUES (?, ?)",
                            (nome, matricula))
                print("Professor cadastrado com sucesso!")

        except sqlite3.Error as e:
            print("Erro ao cadastrar o professor:", e)

    def editar_professor(self, professor_id, novo_nome=None, nova_matricula=None):
        try:
            with con:
                cur = con.cursor()

                if novo_nome:
                    cur.execute("UPDATE Professores SET nome = ? WHERE id_professor = ?",
                                (novo_nome, professor_id))

                if nova_matricula:
                    cur.execute("UPDATE Professores SET matricula = ? WHERE id_professor = ?",
                                (nova_matricula, professor_id))

                print("Professor atualizado com sucesso!")

        except sqlite3.Error as e:
            print("Erro ao editar o professor:", e)

    def ver_dados_professor(self, professor_id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT nome, matricula FROM Professores WHERE id_professor = ?",
                            (professor_id,))
                professor = cur.fetchone()

                if professor:
                    nome, matricula = professor
                    print(f"Dados do professor (ID: {professor_id}):")
                    print(f"Nome: {nome}")
                    print(f"Matrícula: {matricula}")
                else:
                    print("Professor não encontrado.")

        except sqlite3.Error as e:
            print("Erro ao consultar os dados do professor:", e)

    def excluir_professor(self, professor_id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("DELETE FROM Professores WHERE id_professor = ?",
                            (professor_id,))
                print("Professor excluído com sucesso!")

        except sqlite3.Error as e:
            print("Erro ao excluir o professor:", e)

    def visualizar_turmas_professor(self, professor_id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT id_turma, disciplina FROM Turmas WHERE id_professor = ?",
                            (professor_id,))
                turmas = cur.fetchall()

                if turmas:
                    print(f"Turmas do professor (ID: {professor_id}):")
                    for turma in turmas:
                        turma_id, disciplina = turma
                        print(f"ID da turma: {turma_id}")
                        print(f"Disciplina: {disciplina}")
                        print()
                else:
                    print("Não há turmas cadastradas para esse professor.")

        except sqlite3.Error as e:
            print("Erro ao consultar as turmas do professor:", e)

    def visualizar_alunos_turma(self, turma_id):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT a.nome, a.matricula FROM Alunos a JOIN Turmas_Alunos ta ON a.id_aluno = ta.id_aluno WHERE ta.id_turma = ?",
                            (turma_id,))
                alunos = cur.fetchall()

                if alunos:
                    print(f"Alunos da turma (ID: {turma_id}):")
                    for aluno in alunos:
                        nome, matricula = aluno
                        print(f"Nome: {nome}")
                        print(f"Matrícula: {matricula}")
                        print()
                else:
                    print("Não há alunos cadastrados para essa turma.")

        except sqlite3.Error as e:
            print("Erro ao consultar os alunos da turma:", e)
# Criar uma janela Tkinter
janela = Tk()

janela.title("Gestão de Turmas")
janela.geometry("800x700")

    
    
def opcoes_professor():
    btn_cadastrar_professor = Button(janela, text="Cadastrar Professor", command=cadastrar_professor)
    btn_cadastrar_professor.pack()
    
    btn_editar_professor = Button(janela, text="Editar Professor", command=editar_professor)
    btn_editar_professor.pack()
    
    btn_ver_dados_professor = Button(janela, text="Ver dados do Professor", command=ver_dados_professor)
    btn_ver_dados_professor.pack()
    
    btn_excluir_professor = Button(janela, text="Excluir Professor", command=excluir_professor)
    btn_excluir_professor.pack()
    
    btn_visualizar_turmas_professor = Button(janela, text="Ver Turmas do professor", command=ver_turma_professor)
    btn_visualizar_turmas_professor.pack()
    
    btn_visualizar_alunos = Button(janela, text="Ver alunos da turma específica", command=ver_alunos_turma)
    btn_visualizar_alunos.pack()
    
def opcoes_coordenador():
    pass

def opcoes_aluno():
    pass


btn_professor = Button(janela, text="Menu Professor", command=opcoes_professor)
btn_professor.pack()

btn_coordenador = Button(janela, text="Menu Coordenador", command=opcoes_coordenador)
btn_coordenador.pack()
btn_aluno = Button(janela, text="Menu Coordenador", command=opcoes_aluno)
btn_aluno.pack()


# Criar funções para ações dos botões

def cadastrar_professor():
    coordenador = Coordenador()
    nome_professor = entrada_professor_nome.get()
    matricula_professor = entrada_professor_matricula.get()
    try:
        if not nome_professor.replace(' ', '').isalpha():
            raise ValueError("O nome do professor deve ser composto apenas por letras.")
    except ValueError as error:
        # Exibe uma mensagem de erro caso a validação falhe
        tk.messagebox.showerror("Erro", str(error))
        return

    # Verifica se a matrícula contém apenas números
    try:
        int(matricula_professor)
    except ValueError:
        # Exibe uma mensagem de erro caso a validação falhe
        tk.messagebox.showerror("Erro", "A matrícula deve conter apenas números.")
        return

    
    professor = Professor(nome_professor, matricula_professor)
   

    coordenador.cadastrar_professor(nome_professor, matricula_professor)
    
def cadastrar_turma():
    coordenador = Coordenador()
    disciplina = entrada_disciplina.get()
    nome_professor = entrada_professor_nome.get()
    matricula_professor = entrada_professor_matricula.get()
    nome_aluno = entrada_aluno_nome.get()
    matricula_aluno = entrada_aluno_matricula.get()

    professor = Professor(nome_professor, matricula_professor)
    aluno = Aluno(nome_aluno, matricula_aluno)

    coordenador.criar_turma(disciplina, professor, [aluno])

    # Limpar campos de entrada
    entrada_disciplina.delete(0, END)
    entrada_professor_nome.delete(0, END)
    entrada_professor_matricula.delete(0, END)
    entrada_aluno_nome.delete(0, END)
    entrada_aluno_matricula.delete(0, END)


# Adicionar aluno à turma
entrada_professor_nome = tk.Entry(janela)
entrada_professor_nome.pack()

entrada_professor_matricula = tk.Entry(janela)
entrada_professor_matricula.pack()


# Criar botões para as ações

label_professor_id = Label(janela, text="ID do Professor:")
label_professor_id.pack()
entry_professor_id = Entry(janela)
entry_professor_id.pack()


def editar_professor():
    coordenador = Coordenador()
    nome_professor = entrada_professor_nome.get()
    matricula_professor = entrada_professor_matricula.get()
    professor_id = int(entrada_professor_id.get())

    try:
        cur.execute("SELECT nome, matricula FROM Professores WHERE id_professor = ?", (professor_id,))
        professor_info = cur.fetchone()
        if professor_info:
            nome, matricula = professor_info
            entrada_professor_nome.delete(0, END)
            entrada_professor_nome.insert(0, nome)
            entrada_professor_matricula.delete(0, END)
            entrada_professor_matricula.insert(0, matricula)
        else:
            print("Professor não encontrado.")
    except sqlite3.Error as e:
        print("Erro ao buscar informações do professor:", e)


def salvar_edicao_professor():
    professor_id = int(entrada_professor_id.get())
    nome = entrada_professor_nome.get()
    matricula = entrada_professor_matricula.get()

    try:
        cur.execute("UPDATE Professores SET nome = ?, matricula = ? WHERE id_professor = ?", (nome, matricula, professor_id))
        con.commit()
        print("Informações do professor atualizadas com sucesso.")
    except sqlite3.Error as e:
        print("Erro ao salvar as informações do professor:", e)

    entrada_professor_id.delete(0, END)
    entrada_professor_nome.delete(0, END)
    entrada_professor_matricula.delete(0, END)
    

def ver_dados_professor():
    pass

def excluir_professor():
    pass

def ver_turma_professor():
    pass

def ver_alunos_turma():
    id_turma = entrada_id_turma.get()
    coordenador = Coordenador()
    coordenador.visualizar_alunos_turma(id_turma)

    # Limpar campo de entrada
    entrada_id_turma.delete(0, END)
# Campos para editar as informações do professor
label_professor_nome = Label(janela, text="Nome do Professor:")
label_professor_nome.pack()
entry_professor_nome = Entry(janela)
entry_professor_nome.pack()

label_professor_matricula = Label(janela, text="Matrícula do Professor:")
label_professor_matricula.pack()
entry_professor_matricula = Entry(janela)
entry_professor_matricula.pack()

button_salvar_edicao = Button(janela, text="Salvar", command=salvar_edicao_professor)
button_salvar_edicao.pack()
btn_cadastrar_turma = Button(janela, text="Cadastrar Turma", command=cadastrar_turma)
btn_cadastrar_turma.pack()

lbl_id_turma = Label(janela, text="ID da Turma:")
lbl_id_turma.pack()
entrada_id_turma = Entry(janela)
entrada_id_turma.pack()

btn_ver_alunos_turma = Button(janela, text="Ver Alunos da Turma", command=ver_alunos_turma)
btn_ver_alunos_turma.pack()

button_editar_professor = Button(janela, text="Editar Professor", command=editar_professor)
button_editar_professor.pack()
# Executar o loop de eventos do Tkinter
janela.mainloop()
con.close()