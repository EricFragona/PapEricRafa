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

def tema(temaString):
    if temaString == 1:
        ctk.set_appearance_mode = "Light"
        temaString = 2
    else:
        ctk.set_appearance_mode = "Dark"
        temaString = 1

app = ctk.CTk()
temaBool = True
app.geometry("450x350")
app.title("Faça Login ou crie uma nova conta")
ctk.set_appearance_mode("light")
temaString = 1
titulo = ctk.CTkLabel(app, text="No Name Game")
app.resizable(False, False)


#Inserir Dados-----------------------------
user = ctk.CTkLabel(app, text="Nome de Utilizador : ")
user.place(x= 90, y =110)
username = ctk.StringVar()
usernameEntry = ctk.CTkEntry(app, textvariable=username, placeholder_text="Utilizador", width=151)
usernameEntry.place(x=210, y=110)
pin = ctk.CTkLabel(app, text="Pin de 4 dígitos : ")
pin.place(x=110, y=140)
pinvar = ctk.StringVar()
pinEntry = ctk.CTkEntry(app, textvariable=pinvar, show="*", placeholder_text="Pin", width=45 )
pinEntry.place(x=210, y=140)
visivel = ctk.CTkButton(app, text="Mostrar", width=100, command=mostar_pin)
visivel.place(x=260, y=140)

btnTema = ctk.CTkButton(app, text="Tema", width=100, command= lambda: tema(temaString))
btnTema.place(x=325, y=300)
#-----------------------------------




app.mainloop()
