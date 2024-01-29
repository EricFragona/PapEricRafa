import customtkinter as ctk
from CTkMenuBar import *
import sqlite3

# Funções------------------------------------

def frame1():
    user_label = ctk.CTkLabel(root, text="Nome de Utilizador : ")
    user_label.place(x=140, y=160)
    username = ctk.StringVar()
    username_entry = ctk.CTkEntry(root, textvariable=username, placeholder_text="Utilizador", width=151)
    username_entry.place(x=260, y=160)

    pin_label = ctk.CTkLabel(root, text="Pin de 4 dígitos : ")
    pin_label.place(x=160, y=200)
    pin_var = ctk.StringVar()
    pin_entry = ctk.CTkEntry(root, textvariable=pin_var, show="*", placeholder_text="Pin", width=45)
    pin_entry.place(x=260, y=200)

    btn_mostrar = ctk.CTkButton(root, text="Mostrar", width=100, command=lambda: mostrar_pin(pin_entry, btn_mostrar))
    btn_mostrar.place(x=310, y=200)

    btn_login = ctk.CTkButton(root, text="Login", width=100)
    btn_login.place(x=230, y=250)
    
def mostrar_pin(entry, btn):
    if entry.cget('show') == '':
        entry.configure(show='*')
        btn.configure(text='Mostrar')
    else:
        entry.configure(show='')
        btn.configure(text='Esconder')

#def fechar():
#    root.quit()

def nova_conta():
    limpar_conta()

def limpar_conta(widgets):
    for widget in widgets:
        widget.destroy()

    pin_label2 = ctk.CTkLabel(root, text="Repetir Pin : ")
    pin_label2.place(x=185, y=240)
    pin_var2 = ctk.StringVar()
    pin_entry2 = ctk.CTkEntry(root, textvariable=pin_var2, show="*", placeholder_text="Pin", width=45)
    pin_entry2.place(x=260, y=240)

    btn_mostrar2 = ctk.CTkButton(root, text="Mostrar", width=100, command=lambda: mostrar_pin(pin_entry2, btn_mostrar2))
    btn_mostrar2.place(x=310, y=240)
    btn_criar_conta = ctk.CTkButton(root, text="Criar Conta", width=100)
    btn_criar_conta.place(x=230, y=280)

    return pin_label2, pin_entry2, btn_mostrar2, btn_criar_conta

# App---------------------------------------
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
titulo = ctk.CTkLabel(root, text="No Name Game", font=("TkDefaultFont", 30), fg_color="black", corner_radius=20, padx=2, pady=2)
titulo.place(x=160, y=60)
root.resizable(False, False)

# Menu--------------------------------------
menu = CTkMenuBar(root)
button_1 = menu.add_cascade("Definições")
op1 = CustomDropdownMenu(widget=button_1)
op1.add_option(option="Login",)
op1.add_option(option="Nova Conta", command=nova_conta)
op1.add_option(option="Sair", command=fechar)

frame1()
root.mainloop()
