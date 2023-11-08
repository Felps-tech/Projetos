# Windux iAndroid
from tkinter import Tk, Frame, RIGHT, LEFT, Button, Label, Entry, messagebox, DISABLED
import tkinter
from tkinter import ttk
import sqlite3
import datetime

hora_atual = datetime.datetime.now()
janela_principal = Tk()

class sistema():
    def __init__(self):
        self.janela_principal = janela_principal
        self.janela_principal.geometry("650x400+100+100")
        self.janela_principal.title('Sistema:')
        self.janela_principal.resizable(False, False)
        self.abre_login()
        self.janela_principal.mainloop()

    def abre_login(self):
        self.login_frame = Frame(self.janela_principal, width=650, height=400, bg='#152b3c')
        self.login_frame.pack(side=RIGHT)
        self.janela_principal.title('Faça seu login')
        self.labelusuario = Label(self.login_frame, text="Nome de usuário",font=('arial 8 bold'), bg='#152b3c', foreground='white')
        self.labelusuario.place(x=15, y=3)
        self.nome_usuario_login = Entry(self.login_frame, font=('arial 8 bold'), width=35)
        self.nome_usuario_login.place(x=15, y=25)
        self.nome_usuario_login.focus()
        self.labelsenha = Label(self.login_frame,text='Senha:',font=('arial 8 bold'), bg='#152b3c', foreground='white')
        self.labelsenha.place(x=15, y=45)
        self.senha_usuario_login = Entry(self.login_frame, show='*', font=('arial 8 bold'), width=35)
        self.senha_usuario_login.place(x=15, y=67)
        self.senha_usuario_login.focus()
        self.botaocadastrarlogin = Button(self.login_frame, text='Novo',width=10, height=1, bg='#202050', fg='white', font=('arial 8 bold'), command=self.abre_cadastro_usuario).place(x=105, y=95)
        self.botaoentrarsistema = Button(self.login_frame,text='Entrar', width=10, height=1, bg='#202028',fg='white', font=('arial 8 bold'), command=self.abre_login).place(x=15, y=95)
        self.labelinf1 = Label(self.login_frame, text='ANGÉLICO ®',font=('italic 20 bold'), bg='#152b3c',foreground='white').place(x=380,y=25)    
    
    
    def volta_login(self):
        self.cadastro_frame.pack_forget()
        self.cadastro_frame.destroy()
        self.login_frame = Frame(master=self.janela_principal, width=650, height=400, bg='#152b3c')
        self.login_frame.pack(side=RIGHT)
        self.label1 = Label(self.login_frame, text='Nome de usuário :', font=('arial 8 bold'),bg='#152b3c', foreground='white').place(x=15,y=3)
        self.nome_usuario_login = Entry(self.login_frame, font=('arial 8 bold'), width=27).place(x=15, y=25)
        self.labelsenha = Label(self.login_frame, text='Senha :', font=('arial 8 bold'),bg='#152b3c',foreground='white').place(x=15, y=3)
        self.nome_usuario_login = Entry(self.login_frame,font=('arial 8 bold'),width=27).place(x=15, y=25)
        self.labelsenha = Label(self.login_frame, text='Senha :', font=('arial 8 bold'),bg='#152b3c', foreground='white').place(x=15, y=45)
        self.senha_usuario_login = Entry(self.login_frame, show='*', font=('arial 8 bold'), width=27).place(x=15, y=67)
        self.botaocadastrar = Button(self.login_frame, text='Novo', width=10, height=1, bg='#202050', fg='white', font=('arial 8 bold'), command=self.abre_cadastro_usuario).place(x=105, y=95)
        self.botaologin = Button(self.login_frame,text='Entrar', width=10, height=1, bg='#202028',fg='white',font=('arial 8 bold'), command=self.abre_login).place(x=175, y=120)
                

    def abre_cadastro_usuario(self):
        self.login_frame.pack_forget()
        self.login_frame.destroy()
        self.cadastro_frame = Frame(self.janela_principal, width=650, height=400, bg='#152b3c')
        self.cadastro_frame.pack(side=RIGHT)
        self.janela_principal.title('Cadastro de Usuários')
        self.labelcadastro = Label(self.janela_principal, text='Usuário :', font=('arial 8 bold'), bg='#152b3c', foreground='white').place(x=15, y=3)
        self.nousucad = Entry(self.cadastro_frame, font=('arial 8 bold'), width=35)
        self.nousucad.place(x=15, y=25)
        self.nousucad.focus()
        self.labelmailusuario = Label(self.janela_principal, text='E-mail de usuário :', font=('arial 8 bold'), bg='#152b3c', foreground='white').place(x=15, y=45)
        self.emailusucad = Entry(self.cadastro_frame, font=('arial 8 bold'), width=35)
        self.emailusucad.place(x=15, y=65)
        self.labelsenhausuario = Label(self.janela_principal, text='Senha :', font=('arial 8 bold'), bg='#152b3c', foreground='white').place(x=15, y=85)
        self.senhausucad = Entry(self.cadastro_frame, show='*', font=('arial 8 bold'), width=35)
        self.senhausucad.place(x=15, y=105)
        self.botaosalvar = Button(self.cadastro_frame, text='Salvar', width=10, height=1, bg='#3d7b80', fg='white', font=('arial 8 bold'), command=self.cadastrar_usuario_principal).place(x=15, y=135)
        self.botaocancelar = Button(self.cadastro_frame, text='Cancelar', width=10, height=1, bg='#ff4a4a', fg='white', font=('arial 8 bold'), command=self.volta_login).place(x=105, y=135)

    def cadastrar_usuario_principal(self):
        self.abre_login.pack_forget()
        self.janela_principal.destroy()
        self.cadastro_frame_pri = Frame(self.janela_principal, width=650, height=400, bg='#152b3c')
        self.cadastro_frame_pri.pack(side=RIGHT)
        self.janela_principal.title('Cadastro de Usuários')
        self.labenomeusuario = Label(self.cadastro_frame_pri, text='Usuário :', font=('arial 8 bold'), bg='#152b3c', foreground='white').place(x=15, y=3)
        self.nousucad = Entry(self.cadastro_frame_pri, font=('arial 8 bold'), width=70)
        self.nousucad.place(x=15, y=25)
        self.nousucad.focus()
        self.labelemailusuario = Label(self.cadastro_frame_pri, text='E-mail de usuário:', font=('arial 8 bold'), bg='#152b3c', foreground='white').place(x=15, y=45)
        self.emailusucad = Entry(self.cadastro_frame_pri, font=('arial 8 bold'), width=35)
        self.emailusucad.place(x=15, y=65)
        self.labelsenhausuario = Label(self.cadastro_frame_pri, text='Senha', font=('arial 8 bold'), bg='#152b3c', foreground='white').place(x=15, y=85)
        self.senusucad = Entry(self.cadastro_frame_pri, show='*', font=('arial 8 bold'), width=20)
        self.senusucad.place(x=15, y=105)
        self.botaosalvar = Button(self.cadastro_frame_pri, text='Salvar', width=10, height=1, bg='#3d7b80', fg='white', font=('arial 8 bold'), command=self.cadastrar_usuario_principal)
        self.botaosalvar.place(x=15, y=135)
        self.botaocancelar = Button(self.cadastro_frame_pri, text='Cancelar', width=10, height=1, bg='#ff4a4a', fg='white', font=('arial 8 bold'), command=self.abre_login)
        self.botaocadastrar.place(x=105, y=135)
        
sistema()
