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
#App---------------------------------------
root = ctk.CTk()
temaBool = True
root.geometry("450x350")
root.title("Faça Login ou crie uma nova conta")
ctk.set_appearance_mode("system")
temaString = 1
titulo = ctk.CTkLabel(root, text="No Name Game")
root.resizable(False, False)

#Menu--------------------------------------
menu = CTkMenuBar(root)
button_1 = menu.add_cascade("Definições")
op1 = CustomDropdownMenu(widget=button_1)
op1.add_option(option="Login")
op1.add_option(option="Nova Conta")
op1.add_option(option="Sair", command=fechar)


#Inserir Dados-----------------------------
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


root.mainloop()
