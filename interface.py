from tkinter.ttk import *
from tkinter import Label 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import Tk as tk
from turma import *
from PIL import ImageTk, Image

# cores
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # Branca   
co2 = "#e5e5e5"  # grey
co3 = "#00a095"  # Verde
co4 = "#403d3d"   # letra
co6 = "#003452"   # azul
co7 = "#ef5350"   # vermelha

co6 = "#038cfc"   # azul
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

# Criando root
root =Tk()



root.title("Menu Principal")
root.geometry('350x420')
root.configure(background=co2)
root.resizable(width=False, height=False)
frame_detalhes_principal = Frame(root, width=1250, height=2100, bg=co2)
frame_detalhes_principal.grid(row=0, column=0, pady=0, padx=23, sticky=NSEW)

janela_aluno = Toplevel(root)
janela_aluno.title("")
janela_aluno.geometry('850x620')
janela_aluno.configure(background=co1)
janela_aluno.resizable(width=FALSE, height=FALSE)

style = Style(janela_aluno)
style.theme_use("clam")
def show_info(message):
    info_window = Tk()
    info_window.title("Informação")
    info_label = Label(info_window, text=message)
    info_label.pack()
    ok_button = Button(info_window, text="OK", command=info_window.destroy)
    ok_button.pack()
    info_window.mainloop()
    
    
# Criando Frames
frame_logo = Frame(janela_aluno, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela_aluno, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela_aluno, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela_aluno, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela_aluno, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela_aluno, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame Logo

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text='Cadastro de Alunos', width=850, compound=LEFT,relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co7, fg=co1)
app_logo.place(x=0,y=0)
# cadastrar alunos
def novo_aluno():
    global e_nome_aluno
    global e_matricula
    nome = str(e_nome_aluno.get()).title()
    matricula = e_matricula.get()
    try:
        if ' ' not in nome:
            raise ValueError('Digite um nome composto válido')
        if not matricula.isdigit() or ' ' in matricula:
            raise ValueError('Digite uma matrícula válida (apenas números, sem espaços)')
        
        messagebox.showinfo('Sucesso', 'Aluno cadastrado com sucesso')
        a = Coordenador()
        a.adicionar_aluno(nome,matricula)   
        e_nome_aluno.delete(0, END)
        e_matricula.delete(0, END)

    except ValueError as e:
        messagebox.showerror('Erro', str(e))
   
    
    mostrar_alunos()


def buscar_alunos():
    e_nome_procurar = e_nome_aluno.get()
    try:
        with con:
            cur = con.cursor()

            if e_nome_procurar:
                cur.execute("SELECT * FROM Alunos WHERE nome = ?",
                            (e_nome_procurar,))
                result = cur.fetchone()
                if result:
                    # Exibe o resultado em uma mensagem de diálogo
                    messagebox.showinfo('Resultado da Busca', f'Nome: {result[0]}\nMatrícula: {result[1]}')
                else:
                    messagebox.showinfo('Resultado da Busca', 'Nenhum aluno encontrado com esse nome.')

    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao buscar o aluno: {str(e)}')
    

        
def alunos():
    if janela_professor.state == 'zoomed':
        janela_professor.state(newstate='iconic')
    if janela_aluno.state =='iconic':
        janela_aluno.state(newstate='zoomed')
    global e_matricula
    global e_nome_aluno
    
    l_nome = Label(frame_detalhes, text="Nome *",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4)
    l_nome.place(x=4,y=10)
    e_nome_aluno = Entry(frame_detalhes, width=45, justify='left',relief='solid')
    e_nome_aluno.place(x=7,y=40)
    
    l_matricula = Label(frame_detalhes, text="Matrícula *",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4)
    l_matricula.place(x=4,y=70)
    e_matricula = Entry(frame_detalhes, width=35, justify='left',relief='solid')
    e_matricula.place(x=7,y=100)

    
#pegar turmas

#turmas = ['Turma A', 'Turma B']
#turma = []
#for i in turmas:
#    turma.append(i)
#
#l_turma = Label(frame_detalhes, text="Turma *",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4) 
#l_turma.place(x=4, y=140)   
#c_turma = ttk.Combobox(frame_detalhes,width=20, font=('Ivy 8 bold'))
#c_turma['values'] =(turma)
#c_turma.place(x=4, y=170)

#Linha Separatoria

l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
l_linha.place(x=410, y=10)
l_linha = Label(frame_detalhes, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
l_linha.place(x=408, y=10)

#procurar aluno 

l_nome = Label(frame_detalhes, text='Procurar Aluno [Entre com o nome]',height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=437,y=10)
e_nome_procurar = Entry(frame_detalhes, width=17, justify='center', relief='solid', font='Ivy 10')
e_nome_procurar.place(x=440,y=35)

botao_procurar = Button(frame_detalhes, command=buscar_alunos, anchor=CENTER,text="Procurar", width=9, overrelief=RIDGE, font=("Ivy 7 bold"),bg=co1, fg=co0)
botao_procurar.place(x=587, y=35)


##########################

def editar_aluno():
    l_nome_editar = Label(frame_detalhes, text='Editar Aluno [Entre com o nome]',height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome_editar.place(x=608,y=80)
    
    e_nome_editar = Entry(frame_detalhes, width=17, justify='center', relief='solid', font='Ivy 10')
    e_nome_editar.place(x=608,y=120)
    
    l_matricula_editar = Label(frame_detalhes, text='Adicione a nova matrícula',height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_matricula_editar.place(x=608,y=160)
    
    e_matricula_editar = Entry(frame_detalhes, width=17, justify='center', relief='solid', font='Ivy 10')
    e_matricula_editar.place(x=608,y=190)

    def salvar_edicao():
        nome_editar = e_nome_editar.get().title()
        matricula_editar = e_matricula_editar.get()
        for i in df_list_alunos:
           if i in df_list_alunos:
               a.editar_aluno(nome_editar, matricula_editar)
        messagebox.showinfo('Sucesso', 'Aluno atualizado com sucesso')
        e_nome_editar.delete(0, END)
        e_matricula_editar.delete(0, END)
        # Chamar a função mostrar_alunos() para atualizar a tabela de alunos
        mostrar_alunos()

    botao_salvar_edicao = Button(frame_detalhes, command=salvar_edicao, anchor=CENTER, text='Salvar Edição'.upper(), width=15, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar_edicao.place(x=528, y=220)
    e_nome_editar = e_nome_aluno
    e_matricula_editar =e_matricula
    a = Coordenador()
    a.editar_aluno(e_nome_editar,)  
    e_nome_aluno.delete(0, END)
    e_matricula.delete(0, END)
    
    mostrar_alunos()
    
botao_salvar = Button(frame_detalhes, command=novo_aluno, anchor=CENTER, text='Salvar'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
botao_salvar.place(x=437, y=110)
    
botao_atualizar = Button(frame_detalhes,command=editar_aluno, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
botao_atualizar.place(x=437, y=135)
    
botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
botao_deletar.place(x=437, y=160)


    
def mostrar_alunos():
    global df_list_alunos  
    c = Coordenador()
    
    app_nome = Label(frame_tabela, text="Tabela de estudantes", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

  # creating a treeview with dual scrollbars
    list_header = ['id','Nome','Matricula']
  

    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT id_aluno, nome, matricula FROM Alunos")
            df_list_alunos = cur.fetchall()

    except sqlite3.Error as e:
        print("Erro ao obter os alunos:", e)
        df_list_alunos = []  # Set an empty list if there's an error

    global tree_aluno

    tree_aluno = ttk.Treeview(frame_tabela, selectmode="extended",columns=list_header, show="headings")

  # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree_aluno.yview)
  # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree_aluno.xview)

    tree_aluno.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_aluno.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela.grid_rowconfigure(0, weight=12)

    hd=["w","center","e"]
    h=[120,120,120]
    n=0

    for col in list_header:
        tree_aluno.heading(col, text=col.title(), anchor=NW)
        tree_aluno.column(col, width=h[n],anchor=hd[n])
   
    n+=1

    for item in df_list_alunos:
        tree_aluno.insert('', 'end', values=item)
mostrar_alunos()


def coordenador():
    pass
def minimizar_secundaria():
    root.state(newstate='iconic')
    
def minimizar_aluno():
    janela_aluno.state(newstate='iconic')

def minimizar_professor():
    janela_aluno.state(newstate='iconic')

    

    
#funcao para adicionar turmas

#def adicionar():
 #   frame_tabela_turma = Frame(frame_tabela,width=300, height=200, bg=co0)
  #  frame_tabela_turma.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    #frame_tabela_linha = Frame(frame_tabela,width=30, height=200, bg=co3)
    #frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)
    
   #def nova_turma():
   #     nome = e_nome_turma.get()
    #    professor = e_nome
        
        
    
    
   # l_nome = Label(frame_detalhes, text="Nome da turma",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4)
   # l_nome.place(x=4,y=10)
   # e_nome_turma = Entry(frame_detalhes, width=35, justify='left',relief='solid')
   # e_nome_turma.place(x=7,y=40)
    
   # botao_carregar = Button(frame_detalhes, anchor=CENTER, text='Salvar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
   # botao_carregar.place(x=107, y=160)
    
   # botao_atualizar = Button(frame_detalhes, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
   # botao_atualizar.place(x=187, y=160)
    
    #botao_deletar = Button(frame_detalhes, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
   # botao_deletar.place(x=267, y=160)
    
    
    
    

#funcao para salvar 

def salvar():
    print('Salvar')
    


#Função de control
def control(i):
     #cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.pack_forget()  # Ou widget.grid_remove() se estiver usando grid layout

        # Limpar o conteúdo dos widgets dentro do frame_tabela
        for widget in frame_tabela.winfo_children():
            if isinstance(widget, Entry):
                widget.delete(0, END)
            elif isinstance(widget, Text):
                widget.delete('1.0', END)
        
    
  
    



# criando botoes
app_img_cadastro = Image.open('adicionar.png')
app_img_cadastro = app_img_cadastro.resize((14,14))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text='Cadastro', width=80,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=0,y=30)
app_retornar = Button(frame_dados, command=janela_aluno.destroy,  text='Retornar', width=12,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_retornar.place(x=0,y=30)
app_minimizar = Button(frame_dados, command=minimizar_aluno,  text='Minimizar', width=12,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_minimizar.place(x=150,y=30)

#--------------------------------------------------------------------------#
#app_img_adicionar = Image.open('adicionar.png')
#app_img_adicionar = app_img_adicionar.resize((14,14))
#app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
#app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text='Adicionar', width=80,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
#app_adicionar.place(x=143,y=30)


janela_professor = Toplevel(root)
janela_professor.title("")
janela_professor.geometry('850x620')
janela_professor.configure(background=co1)
janela_professor.resizable(width=FALSE, height=FALSE)

style = Style(janela_professor)
style.theme_use("clam")
# Criando Frames
frame_logo_professor = Frame(janela_professor, width=850, height=52, bg=co6)
frame_logo_professor.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela_professor, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados_professor = Frame(janela_professor, width=850, height=65, bg=co1)
frame_dados_professor.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela_professor, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes_professor = Frame(janela_professor, width=850, height=200, bg=co1)
frame_detalhes_professor.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela_professor = Frame(janela_professor, width=850, height=200, bg=co1)
frame_tabela_professor.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame Logo

app_lg_professor = Image.open('logo_professor.png')
app_lg_professor = app_lg_professor.resize((50,50))
app_lg_professor = ImageTk.PhotoImage(app_lg_professor)
app_logo_professor = Label(frame_logo_professor, image=app_lg_professor, text='Cadastro de Professores', width=850, compound=LEFT,relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co7, fg=co1)
app_logo_professor.place(x=0,y=0)
# cadastrar alunos
def novo_professor():
    global e_nome_professor
    global e_matricula_professor
    nome = str(e_nome_professor.get()).title()
    matricula = e_matricula_professor.get()
    try:
        if ' ' not in nome:
            raise ValueError('Digite um nome composto válido')
        
        if not matricula.isdigit() or ' ' in matricula:
            raise ValueError('Digite uma matrícula válida (apenas números, sem espaços)')
    
        messagebox.showinfo('Sucesso', 'Professor cadastrado com sucesso')
        a = Coordenador()
        a.cadastrar_professor(nome,matricula)   
        e_nome_professor.delete(0, END)
        e_matricula_professor.delete(0, END)

    except ValueError as e:
        messagebox.showerror('Erro', str(e))


    mostrar_professores()


def buscar_professores():
    e_nome_procurar = e_nome_professor.get()
    try:
        with con:
            cur = con.cursor()

        if e_nome_procurar:
            cur.execute("SELECT * FROM Professores WHERE id_professor = ?",
                        (e_nome_procurar,))
            result = cur.fetchone()
            if result:
                # Exibe o resultado em uma mensagem de diálogo
                messagebox.showinfo('Resultado da Busca', f'Nome: {result[0]}\nMatrícula: {result[1]}')
            else:
                messagebox.showinfo('Resultado da Busca', 'Nenhum professor encontrado com esse nome.')

    except Exception as e:
        messagebox.showerror('Erro', f'Ocorreu um erro ao buscar o professor: {str(e)}')


    
def professores():
    janela_aluno.state(newstate='iconic')
    global e_matricula_professor
    global e_nome_professor

    l_nome = Label(frame_detalhes_professor, text="Nome *",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4)
    l_nome.place(x=4,y=10)
    e_nome_professor = Entry(frame_detalhes_professor, width=45, justify='left',relief='solid')
    e_nome_professor.place(x=7,y=40)

    l_matricula_professor = Label(frame_detalhes_professor, text="Matrícula *",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4)
    l_matricula_professor.place(x=4,y=70)
    e_matricula_professor = Entry(frame_detalhes_professor, width=35, justify='left',relief='solid')
    e_matricula_professor.place(x=7,y=100)


#pegar turmas

#turmas = ['Turma A', 'Turma B']
#turma = []
#for i in turmas:
#    turma.append(i)
#
#l_turma = Label(frame_detalhes, text="Turma *",height=1, anchor=NW, font=('Ivy 10'), bg =co1, fg=co4) 
#l_turma.place(x=4, y=140)   
#c_turma = ttk.Combobox(frame_detalhes,width=20, font=('Ivy 8 bold'))
#c_turma['values'] =(turma)
#c_turma.place(x=4, y=170)

#Linha Separatoria

    l_linha = Label(frame_detalhes_professor, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co0, fg=co0)
    l_linha.place(x=410, y=10)
    l_linha = Label(frame_detalhes_professor, relief=GROOVE, text='h', width=1, height=100, anchor=NW, font=('Ivy 1'), bg=co1, fg=co0)
    l_linha.place(x=408, y=10)

#procurar aluno 

    l_nome = Label(frame_detalhes_professor, text='Procurar Aluno [Entre com o nome]',height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=437,y=10)
    e_nome_procurar = Entry(frame_detalhes_professor, width=17, justify='center', relief='solid', font='Ivy 10')
    e_nome_procurar.place(x=440,y=35)

    botao_procurar = Button(frame_detalhes_professor, command=buscar_professores, anchor=CENTER,text="Procurar", width=9, overrelief=RIDGE, font=("Ivy 7 bold"),bg=co1, fg=co0)
    botao_procurar.place(x=587, y=35)


##########################

def editar_professor():
    l_nome_editar = Label(frame_detalhes_professor, text='Editar Professor [Entre com o nome]',height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome_editar.place(x=608,y=80)

    e_nome_editar = Entry(frame_detalhes_professor, width=17, justify='center', relief='solid', font='Ivy 10')
    e_nome_editar.place(x=608,y=120)

    l_matricula_professor_editar = Label(frame_detalhes_professor, text='Adicione a nova matrícula',height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_matricula_professor_editar.place(x=608,y=160)

    e_matricula_professor_editar = Entry(frame_detalhes, width=17, justify='center', relief='solid', font='Ivy 10')
    e_matricula_professor_editar.place(x=608,y=190)

    def salvar_edicao_professor():
        nome_editar = e_nome_editar.get().title()
        matricula_editar = e_matricula_professor_editar.get()
        for i in df_list_professor:
            if i in df_list_professor:
                a.editar_professor(nome_editar, matricula_editar)
        messagebox.showinfo('Sucesso', 'Professor atualizado com sucesso')
        e_nome_editar.delete(0, END)
        e_matricula_professor_editar.delete(0, END)
    # Chamar a função mostrar_alunos() para atualizar a tabela de alunos
    mostrar_professores()

    botao_salvar_edicao = Button(frame_detalhes_professor, command=salvar_edicao_professor, anchor=CENTER, text='Salvar Edição'.upper(), width=15, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
    botao_salvar_edicao.place(x=528, y=220)
    e_nome_editar = e_nome_professor
    e_matricula_professor_editar =e_matricula_professor
    a = Coordenador()
    a.editar_professor(e_nome_editar,)  
    e_nome_professor.delete(0, END)
    e_matricula_professor_editar.delete(0, END)

    mostrar_professores()

botao_salvar = Button(frame_detalhes_professor, command=novo_professor, anchor=CENTER, text='Salvar'.upper(), width=9, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co3, fg=co1)
botao_salvar.place(x=437, y=110)

botao_atualizar = Button(frame_detalhes_professor,command=editar_professor, anchor=CENTER, text='Atualizar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co6, fg=co1)
botao_atualizar.place(x=437, y=135)

botao_deletar = Button(frame_detalhes_professor, anchor=CENTER, text='Deletar'.upper(), width=10, overrelief=RIDGE, font=('Ivy 7 bold'), bg=co7, fg=co1)
botao_deletar.place(x=437, y=160)
app_retornar = Button(frame_dados_professor, command=janela_professor.destroy,  text='Retornar', width=12,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_retornar.place(x=0,y=30)
app_minimizar = Button(frame_dados_professor, command=minimizar_aluno,  text='Minimizar', width=12,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_minimizar.place(x=150,y=30)



def mostrar_professores():
    global df_list_professor  
    c = Coordenador()
    
    app_nome_professor = Label(frame_tabela_professor, text="Tabela de Professores", height=1,pady=0, padx=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
    app_nome_professor.grid(row=0, column=0, padx=0, pady=10, sticky=NSEW)

# creating a treeview with dual scrollbars
    list_header = ['id','Nome','Matricula']


    try:
        with con:
            cur = con.cursor()
            cur.execute("SELECT id_professor, nome, matricula FROM Professores")
            df_list = cur.fetchall()

    except sqlite3.Error as e:
        print("Erro ao obter os professores:", e)
        df_list = []  # Set an empty list if there's an error

    global tree_professor

    tree_professor = ttk.Treeview(frame_tabela_professor, selectmode="extended",columns=list_header, show="headings")

# vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela_professor, orient="vertical", command=tree_professor.yview)
# horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela_professor, orient="horizontal", command=tree_professor.xview)

    tree_professor.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree_professor.grid(column=0, row=1, sticky='nsew')
    vsb.grid(column=1, row=1, sticky='ns')
    hsb.grid(column=0, row=2, sticky='ew')
    frame_tabela_professor.grid_rowconfigure(0, weight=12)

    hd=["w","center","e"]
    h=[120,120,120]
    n=0

    for col in list_header:
        tree_professor.heading(col, text=col.title(), anchor=NW)
# adjust the column's width to the header string
        tree_aluno.column(col, width=h[n],anchor=hd[n])

    n+=1

    for item in df_list:
        tree_professor.insert('', 'end', values=item)
mostrar_professores()
    
botao_minimizar_secundaria = Button(frame_detalhes_principal,anchor=CENTER, text="Minimizar", command=minimizar_secundaria, width=15, overrelief=RIDGE)
botao_minimizar_secundaria.place(x=80, y=50)
botao_aluno = Button(frame_detalhes_principal,anchor=CENTER, text="Menu Aluno", command=alunos, width=15, overrelief=RIDGE)
botao_aluno.place(x=80, y=100)
botao_professor = Button(frame_detalhes_principal,anchor=CENTER, text="Menu Professor", command=professores ,width=15,overrelief=RIDGE)
botao_professor.place(x=80, y=150)
botao_coordenador = Button(frame_detalhes_principal, text="Menu Coordenador", command=coordenador, width=15, overrelief=RIDGE)
botao_coordenador.place(x=80, y=200)
# Executando a root



root.mainloop()


