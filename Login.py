import customtkinter as ctk
from CTkMenuBar import *
import sqlite3

#Funções------------------------------------
def mostar_pin():
    if pinEntry.cget('show') == '':
        pinEntry.configure(show='*')
        BtnMostrar.configure(text='Mostrar')
    else:
        pinEntry.configure(show='')
        BtnMostrar.configure(text='Esconder')

def fechar():
    root.quit()

def criar_login():
    global user, usernameEntry, pin, BtnLogin, pinEntry, BtnMostrar
    user = ctk.CTkLabel(root, text="Nome de Utilizador : ")
    user.place(x= 90, y =110)
    username = ctk.StringVar()
    usernameEntry = ctk.CTkEntry(root, textvariable=username, placeholder_text="Utilizador", width=151)
    usernameEntry.place(x=210, y=110)
    pin = ctk.CTkLabel(root, text="Pin de 4 dígitos : ")
    pin.place(x=110, y=150)
    pinvar = ctk.StringVar()
    pinEntry = ctk.CTkEntry(root, textvariable=pinvar, show="*", placeholder_text="Pin", width=45 )
    pinEntry.place(x=210, y=150)
    BtnMostrar = ctk.CTkButton(root, text="Mostrar", width=100, command=mostar_pin)
    BtnMostrar.place(x=260, y=150)
    BtnLogin = ctk.CTkButton(root, text="Login", width=100)
    BtnLogin.place(x=180, y=190)
    
def limpar_login():
    user.destroy()
    usernameEntry.destroy()
    pin.destroy()
    pinEntry.destroy()
    BtnMostrar.destroy()
    BtnLogin.destroy()
#App---------------------------------------
root = ctk.CTk()
w = 450 # width for the Tk root
h = 350
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Faça Login ou crie uma nova conta")
ctk.set_appearance_mode("system")
temaString = 1
titulo = ctk.CTkLabel(root, text="No Name Game")
root.resizable(False, False)


#Menu--------------------------------------
menu = CTkMenuBar(root)
button_1 = menu.add_cascade("Definições")
op1 = CustomDropdownMenu(widget=button_1)
op1.add_option(option="Login", command=criar_login)
op1.add_option(option="Nova Conta", command=limpar_login)
op1.add_option(option="Sair", command=fechar)



criar_login()
root.mainloop()

