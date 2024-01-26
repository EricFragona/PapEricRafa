import tkinter as tk
from tkinter import messagebox
import json

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("No Name Game - Login ou criação de conta")
        w = 550
        h = 350
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))


        self.login_frame = tk.Frame(self.root)
        self.register_frame = tk.Frame(self.root)

        self.create_widgets()

    def create_widgets(self):
        # Rótulo do título
        title_label = tk.Label(self.root, text="No Name Game", font=("Helvetica", 25, "bold"))
        title_label.place(relx=0.5, y=50, anchor=tk.CENTER)
        
        # Configurar a estrutura da janela
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Widgets para o frame de login
        tk.Label(self.login_frame, text="Login").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.login_frame, text="Usuário:").grid(row=1, column=0, sticky="e")
        tk.Label(self.login_frame, text="Senha:").grid(row=2, column=0, sticky="e")

        self.login_user_entry = tk.Entry(self.login_frame)
        self.login_password_entry = tk.Entry(self.login_frame, show="*")
        self.login_user_entry.grid(row=1, column=1, sticky="w")
        self.login_password_entry.grid(row=2, column=1, sticky="w")

        tk.Button(self.login_frame, text="Entrar", command=self.login).grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="Criar Nova Conta!", command=self.show_register_frame).grid(row=4, column=0, columnspan=2, pady=10)
        
        # Widgets para o frame de registro
        tk.Label(self.register_frame, text="Registro").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.register_frame, text="Novo Usuário:").grid(row=1, column=0, sticky="e")
        tk.Label(self.register_frame, text="Nova Senha:").grid(row=2, column=0, sticky="e")
        tk.Label(self.register_frame, text="Repetir Senha:").grid(row=3, column=0, sticky="e")

        self.register_user_entry = tk.Entry(self.register_frame)
        self.register_password_entry = tk.Entry(self.register_frame, show="*")
        self.repetir_password_entry = tk.Entry(self.register_frame, show="*")
        self.register_user_entry.grid(row=1, column=1, sticky="w")
        self.register_password_entry.grid(row=2, column=1, sticky="w")
        self.repetir_password_entry.grid(row=3, column=1, sticky="w")

        tk.Button(self.register_frame, text="Registrar", command=self.register).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.register_frame, text="Já tenho conta! ", command=self.show_login_frame).grid(row=5, column=0, columnspan=2, pady=10)

        # Inicialmente, ocultar o frame de registro
        self.show_login_frame()

    def login(self):
        user = self.login_user_entry.get()
        password = self.login_password_entry.get()

        # Verificar se o usuário e senha correspondem
        if self.check_credentials(user, password):
            messagebox.showinfo("Login", "Login bem-sucedido!")
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos.")

    def register(self):
        user = self.register_user_entry.get()
        password = self.register_password_entry.get()
        password2 = self.repetir_password_entry.get()
        
        # Verificar se os campos estão em branco
        if not user or not password:
            messagebox.showerror("Registro", "Por favor, preencha todos os campos.")
            return

        if password != password2:
            messagebox.showerror("Registro", "As Passwords não coincidem!")
            return
        # Adicionar novo usuário ao arquivo JSON
        users = self.load_users()

        # Verificar se o usuário já existe
        if user in users:
            messagebox.showerror("Registro", "Usuário já existe. Por favor, escolha outro.")
        else:
            users[user] = password
            self.save_users(users)
            messagebox.showinfo("Registro", "Registro bem-sucedido!")

            # Após o registro, voltar para o frame de login
            self.show_login_frame()

    def check_credentials(self, user, password):
        users = self.load_users()
        return user in users and users[user] == password

    def load_users(self):
        try:
            with open("users.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self, users):
        with open("users.json", "w") as file:
            json.dump(users, file)

    def show_register_frame(self):
        self.login_frame.place_forget()  # Ocultar o frame de login
        self.register_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Exibir o frame de registro

    def show_login_frame(self):
        self.register_frame.place_forget()  # Ocultar o frame de registro
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Exibir o frame de login

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    
    root.mainloop()
