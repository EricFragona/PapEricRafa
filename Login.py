from tkinter import *
import sqlite3


app = Tk()
app.geometry("300x300")
app.title("Faça Login ou crie uma nova conta")

titulo = Label(text="No Name Game")

user = Label(app, text="Nome de Utilizador: ").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(app, textvariable=username).grid(row=0, column=1)

pin = Label(app, text="Pin: ").grid(row=2, column=0)
username = StringVar()
pinEntry = Entry(app, textvariable=username, show="*").grid(row=2, column=1)









app.mainloop()
