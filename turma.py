import sqlite3
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
                    matricula TEXT UNIQUE
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
                    matricula TEXT UNIQUE
                  
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
        self._id_turma = None
    

class Coordenador:
    def __init__(self):
        self._id_turma = None
        self._alunos=[]
        self.nova_lista =[]
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
                self.set_id_turma(turma_id)

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
    
    
    
    def adicionar_aluno(self, nome, matricula):
        aluno = Aluno(nome, matricula)
        self._alunos.append(aluno)
        cur.execute("INSERT INTO Alunos (nome,matricula) VALUES (?, ?)", (nome, matricula))
        con.commit()

        
    def remover_aluno(self, aluno_id):
        self._alunos = [aluno for aluno in self._alunos if aluno.id_aluno != aluno_id]
        self._alunos.remove(aluno_id)
        cur.execute("DELETE FROM Turmas_Alunos WHERE id_turma = ? AND id_aluno = ?", (self.id_turma, aluno_id))
        con.commit()
        
    def ver_alunos(self):
        
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT nome, matricula FROM Alunos INNER JOIN Turmas_Alunos ON Alunos.id_aluno = Turmas_Alunos.id_aluno WHERE Turmas_Alunos.id_turma = ?", (self._id_turma,))
                alunos = cur.fetchall()
                for aluno in alunos:
                    cur.__str__(aluno)

        except sqlite3.Error as e:
            print("Erro ao obter os alunos da turma:", e)
    
    def set_id_turma(self, id_turma):
        self._id_turma = id_turma
        
    def editar_aluno(self, nome_aluno, novo_nome=None, nova_matricula=None):
        try:
            with con:
                cur = con.cursor()

                if novo_nome:
                    cur.execute("UPDATE Alunos SET nome = ? WHERE nome = ?",
                            (novo_nome, nome_aluno))

                if nova_matricula:
                    cur.execute("UPDATE Alunos SET matricula = ? WHERE nome = ?",
                            (nova_matricula, nome_aluno))

                print("Aluno atualizado com sucesso!")
        except Exception as e:
            print("Ocorreu um erro ao atualizar o aluno:", str(e))
    
    def cadastrar_professor(self, nome, matricula):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO Professores (nome, matricula) VALUES (?, ?)",
                            (nome, matricula))
                print("Professor cadastrado com sucesso!")

        except sqlite3.Error as e:
            print("Erro ao cadastrar o professor:", e)

    def editar_professor(self, nome_professor, novo_nome=None, nova_matricula=None):
        try:
            with con:
                cur = con.cursor()

                if novo_nome:
                    cur.execute("UPDATE Professores SET nome = ? WHERE nome = ?",
                            (novo_nome, nome_professor))

                if nova_matricula:
                    cur.execute("UPDATE Professores SET matricula = ? WHERE nome = ?",
                            (nova_matricula, nome_professor))

                print("Professor atualizado com sucesso!")
        except Exception as e:
            print("Ocorreu um erro ao atualizar o professor:", str(e))


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
            
        finally:
            con.close()            
