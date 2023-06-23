from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd

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

# Criando janela
janela = Tk()
janela.title("")
janela.geometry('850x620')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Criando Frames
frame_logo = Frame(janela, width=850, height=52, bg=co6)
frame_logo.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=680)

frame_dados = Frame(janela, width=850, height=65, bg=co1)
frame_dados.grid(row=2, column=0, pady=0, padx=0, sticky=NSEW)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=3, columnspan=1, ipadx=680)

frame_detalhes = Frame(janela, width=850, height=200, bg=co1)
frame_detalhes.grid(row=4, column=0, pady=0, padx=10, sticky=NSEW)

frame_tabela = Frame(janela, width=850, height=200, bg=co1)
frame_tabela.grid(row=5, column=0, pady=0, padx=10, sticky=NSEW)

# Trabalhando no frame Logo

app_lg = Image.open('logo.png')
app_lg = app_lg.resize((50,50))
app_lg = ImageTk.PhotoImage(app_lg)
app_logo = Label(frame_logo, image=app_lg, text='Cadastro de Alunos', width=850, compound=LEFT,relief=RAISED, anchor=NW, font=('Ivy 15 bold'), bg=co7, fg=co1)
app_logo.place(x=0,y=0)
# cadastrar alunos
def alunos():
    print('Aluno')

#funcao para adicionar turmas

def adicionar():
    frame_tabela_turma = Frame(frame_tabela,width=300, height=200, bg=co0)
    frame_tabela_turma.grid(row=0, column=0, pady=0, padx=0, sticky=NSEW)
    
    frame_tabela_linha = Frame(frame_tabela,width=30, height=200, bg=co3)
    frame_tabela_linha.grid(row=0, column=1, pady=0, padx=10, sticky=NSEW)
    
#funcao para salvar 

def salvar():
    print('Salvar')
    


#Função de control
def control(i):
    # cadastro de aluno
    if i == 'cadastro':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
            
        #chamando a funcao aluno
        alunos()
    
  
    # cadastro de aluno
    if i == 'adicionar':
        for widget in frame_detalhes.winfo_children():
            widget.destroy()
        
        for widget in frame_tabela.winfo_children():
            widget.destroy()
            
        #chamando a funcao aluno
        adicionar()
        



# criando botoes
app_img_cadastro = Image.open('adicionar.png')
app_img_cadastro = app_img_cadastro.resize((14,14))
app_img_cadastro = ImageTk.PhotoImage(app_img_cadastro)
app_cadastro = Button(frame_dados, command=lambda:control('cadastro'), image=app_img_cadastro, text='Cadastro', width=80,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_cadastro.place(x=0,y=30)

app_img_adicionar = Image.open('adicionar.png')
app_img_adicionar = app_img_adicionar.resize((14,14))
app_img_adicionar = ImageTk.PhotoImage(app_img_adicionar)
app_adicionar = Button(frame_dados, command=lambda:control('adicionar'), image=app_img_adicionar, text='Adicionar', width=80,compound=LEFT, overrelief=RIDGE, font=('Ivy 11'), bg=co1, fg=co0)
app_adicionar.place(x=143,y=30)



# Executando a janela
janela.mainloop()
