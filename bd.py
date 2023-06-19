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
    
con.commit()
con.close()