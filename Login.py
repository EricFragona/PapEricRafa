import customtkinter as ctk
import sqlite3

#Funções-----------------------------------
def mostar_pin():
    if pinEntry.cget('show') == '':
        pinEntry.configure(show='*')
        visivel.configure(text='Mostrar')
    else:
        pinEntry.configure(show='')
        visivel.configure(text='Esconder')

def tema():
    if ctk.set_appearance_mode == "Dark":
        ctk.set_appearance_mode = "Light"
    else:
        ctk.set_appearance_mode = "Dark"

app = ctk.CTk()
app.geometry("450x350")
app.title("Faça Login ou crie uma nova conta")
ctk.set_appearance_mode("dark")
titulo = ctk.CTkLabel(app, text="No Name Game")


#Inserir Dados-----------------------------
user = ctk.CTkLabel(app, text="Nome de Utilizador: ")
user.place(x= 90, y =110)
username = ctk.StringVar()
usernameEntry = ctk.CTkEntry(app, textvariable=username, placeholder_text="Utilizador", width=166)
usernameEntry.place(x=210, y=110)
pin = ctk.CTkLabel(app, text="Pin: ")
pin.place(x=175, y=140)
pinvar = ctk.StringVar()
pinEntry = ctk.CTkEntry(app, textvariable=pinvar, show="*", placeholder_text="Pin", width=45 )
pinEntry.place(x=210, y=140)
visivel = ctk.CTkButton(app, text="Mostrar", width=100, command=mostar_pin)
visivel.place(x=260, y=160)

btnTema = ctk.CTkButton(app, text="tema", width=100, command=tema)
btnTema.place(x=260, y=140)
#-----------------------------------




app.mainloop()
