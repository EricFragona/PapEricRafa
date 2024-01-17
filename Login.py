import customtkinter as ctk
from CTkMenuBar import *
import sqlite3



#Funções------------------------------------
def mostar_pin(entry, btn):
    if entry.cget('show') == '':
        entry.configure(show='*')
        btn.configure(text='Mostrar')
    else:
        entry.configure(show='')
        btn.configure(text='Esconder')

def fechar():
    root.quit()

def criar_login():
    global user, usernameEntry, pin, BtnLogin, pinEntry, BtnMostrar
    if 'user' in globals():
        limpar_login()
    user = ctk.CTkLabel(root, text="Nome de Utilizador : ")
    user.place(x= 140, y =160)
    username = ctk.StringVar()
    usernameEntry = ctk.CTkEntry(root, textvariable=username, placeholder_text="Utilizador", width=151)
    usernameEntry.place(x=260, y=160)
    
    pin = ctk.CTkLabel(root, text="Pin de 4 dígitos : ")
    pin.place(x=160, y=200)
    pinvar = ctk.StringVar()
    pinEntry = ctk.CTkEntry(root, textvariable=pinvar, show="*", placeholder_text="Pin", width=45 )
    pinEntry.place(x=260, y=200)
    
    BtnMostrar = ctk.CTkButton(root, text="Mostrar", width=100, command=mostar_pin(pinEntry,BtnMostrar))
    BtnMostrar.place(x=310, y=200)
    BtnLogin = ctk.CTkButton(root, text="Login", width=100)
    BtnLogin.place(x=230, y=250)
    
def limpar_login():
    user.destroy()
    usernameEntry.destroy()
    pin.destroy()
    pinEntry.destroy()
    BtnMostrar.destroy()
    BtnLogin.destroy()
    
def nova_conta():
    limpar_login()
    user = ctk.CTkLabel(root, text="Nome de Utilizador : ")
    user.place(x= 140, y =160)
    username = ctk.StringVar()
    usernameEntry = ctk.CTkEntry(root, textvariable=username, placeholder_text="Utilizador", width=151)
    usernameEntry.place(x=260, y=160)
    
    pin = ctk.CTkLabel(root, text="Pin de 4 dígitos : ")
    pin.place(x=160, y=200)
    pinvar = ctk.StringVar()
    pinEntry2 = ctk.CTkEntry(root, textvariable=pinvar, show="*", placeholder_text="Pin", width=45 )
    pinEntry2.place(x=260, y=200)
    pin2 = ctk.CTkLabel(root, text="Repetir Pin : ")
    pin2.place(x=185, y=240)
    pinvar2 = ctk.StringVar()
    pinEntry3 = ctk.CTkEntry(root, textvariable=pinvar2, show="*", placeholder_text="Pin", width=45 )
    pinEntry3.place(x=260, y=240)
    
    BtnMostrar2 = ctk.CTkButton(root, text="Mostrar", width=100, command=mostar_pin(pinEntry2,BtnMostrar2))
    BtnMostrar2.place(x=310, y=200)
    BtnMostrar3 = ctk.CTkButton(root, text="Mostrar", width=100, command=mostar_pin(pinEntry3,BtnMostrar3))
    BtnMostrar3.place(x=310, y=240)
    BtnLogin = ctk.CTkButton(root, text="Login", width=100)
    BtnLogin.place(x=230, y=250)
#App---------------------------------------
root = ctk.CTk()
w = 550
h = 450
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.title("Faça Login ou crie uma nova conta")
ctk.set_appearance_mode("dark")
temaString = 1
titulo = ctk.CTkLabel(root, text="No Name Game", font=("TkDefaultFont",30), fg_color="black", corner_radius=20, padx=2, pady=2)
titulo.place(x=160, y=60)
root.resizable(False, False)



#Menu--------------------------------------
menu = CTkMenuBar(root)
button_1 = menu.add_cascade("Definições")
op1 = CustomDropdownMenu(widget=button_1)
op1.add_option(option="Login", command=criar_login)
op1.add_option(option="Nova Conta", command=nova_conta)
op1.add_option(option="Sair", command=fechar)



criar_login()
root.mainloop()

