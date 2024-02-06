import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
import Sqlite as Sq

class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.title("No Name Game - Login ou criação de conta")
        style = ttk.Style()
        style.configure("TButton", padding=5, relief="flat", font=("Arial", 12, "bold"))
        w = 650
        h = 350
        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        root.resizable(False, False)
        root.config(bg="#1e3a56")
        self.login_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.registo_frame = tk.Frame(self.root, bg="#f2f2f2")
        self.opcoes_frame = tk.Frame(self.root, bg="#f2f2f2")

        self.create_widgets()
        self.addBotaoVerSenhas()

    def create_widgets(self):
        title_label = tk.Label(self.root, text="No Name Game", font=("Helvetica", 25, "bold"), bg="#1e3a56", fg="white")
        title_label.place(relx=0.5, y=25, anchor=tk.CENTER)

        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.registo_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.opcoes_frame.place(x=0.5, y=0.5, anchor=tk.CENTER)

        tk.Label(self.login_frame, text="Login", font=("Arial", 16, "bold"), bg="#f2f2f2").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.login_frame, text="Utilizador:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.login_frame, text="Senha:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky="e", pady=5)

        self.login_user_entry = tk.Entry(self.login_frame, font=("Arial", 12))
        self.login_password_entry = tk.Entry(self.login_frame, show="*", font=("Arial", 12))
        self.login_user_entry.grid(row=1, column=1, sticky="w", pady=5)
        self.login_password_entry.grid(row=2, column=1, sticky="w", pady=5)

        tk.Button(self.login_frame, text="Entrar", command=self.verificar_login, font=("Arial", 12, "bold"), bg="#4caf50", fg="white").grid(row=3, column=0, columnspan=2, pady=10)
        tk.Button(self.login_frame, text="Criar Nova Conta!", command=self.show_register_frame, font=("Arial", 12, "underline"), bg="#1e3a56", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

        tk.Label(self.registo_frame, text="Registro", font=("Arial", 16, "bold"), bg="#f2f2f2").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(self.registo_frame, text="Utilizador:", font=("Arial", 12), bg="#f2f2f2").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(self.registo_frame, text="Nova Senha:", font=("Arial", 12), bg="#f2f2f2").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(self.registo_frame, text="Repetir Senha:", font=("Arial", 12), bg="#f2f2f2").grid(row=3, column=0, sticky="e", pady=5)

        self.register_user_entry = tk.Entry(self.registo_frame, font=("Arial", 12))
        self.register_password_entry = tk.Entry(self.registo_frame, show="*", font=("Arial", 12))
        self.repetir_password_entry = tk.Entry(self.registo_frame, show="*", font=("Arial", 12))
        self.register_user_entry.grid(row=1, column=1, sticky="w", pady=5)
        self.register_password_entry.grid(row=2, column=1, sticky="w", pady=5)
        self.repetir_password_entry.grid(row=3, column=1, sticky="w", pady=5)

        tk.Button(self.registo_frame, text="Registrar", command=self.register, font=("Arial", 12, "bold"), bg="#4caf50", fg="white").grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.registo_frame, text="Já tenho conta! ", command=self.show_login_frame, font=("Arial", 12, "underline"), bg="#1e3a56", fg="white").grid(row=5, column=0, columnspan=2, pady=10)

        tk.Label(self.opcoes_frame, text="Opções", font=("Arial", 14, "bold"), bg="#f2f2f2").grid(row=2, column=0, columnspan=4, pady=5)
        tk.Button(self.opcoes_frame, text="Jogar!!!", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", width=26).grid(row=3, column=0, columnspan=4, pady=10)
        tk.Button(self.opcoes_frame, text="Alterar Password", command=self.alterar_senha, font=("Arial", 11, "bold"), bg="#f39c12", fg="white", width=13).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.opcoes_frame, text="Alterar Nome", font=("Arial", 11, "bold"), bg="#f39c12", fg="white", width=14).grid(row=4, column=2, columnspan=2, pady=10)
        tk.Button(self.opcoes_frame, text="Apagar Conta", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", width=25).grid(row=5, column=0, columnspan=4, pady=10)
        tk.Button(self.opcoes_frame, text="Logout", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", width=25).grid(row=6, column=0, columnspan=4, pady=10)

        self.show_login_frame()
        
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
        else:
            messagebox.showinfo("Registro", "Registro bem-sucedido!")
            Sq.criarConta(user, password)
            self.show_login_frame()

    def show_register_frame(self):
        self.login_frame.place_forget()
        self.opcoes_frame.place_forget()
        self.registo_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.login_password_entry.delete(0, 'end')
        self.login_user_entry.delete(0, 'end')
         
    def show_login_frame(self):
        self.registo_frame.place_forget()
        self.opcoes_frame.place_forget()
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.register_user_entry.delete(0, 'end')
        self.register_password_entry.delete(0, 'end')
        self.repetir_password_entry.delete(0, 'end')
        
    def show_opcoes_frame(self):
        self.login_frame.place_forget()
        self.registo_frame.place_forget()
        self.opcoes_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
    def ocultarSenha(self):
        self.register_password_entry.config(show="*")
        self.repetir_password_entry.config(show="*")
        self.login_password_entry.config(show="*")

    def mostrarSenha(self):
        self.register_password_entry.config(show="")
        self.repetir_password_entry.config(show="")
        self.login_password_entry.config(show="")
    
    def addBotaoVerSenhas(self):
        self.ver = tk.PhotoImage(file=r'C:\Users\aluno\Documents\GitHub\PapEricRafa\Imagens\olhoAberto.png').subsample(17)
        tk.Button(self.root, text="Mostrar", image=self.ver, compound="left", command=self.mostrarSenha, bd=2, relief="raised", font=("Arial", 12, "bold"), bg="#4caf50", fg="white", width=106).place(relx=0.05, rely=0.37)
        self.esconder = tk.PhotoImage(file=r'C:\Users\aluno\Documents\GitHub\PapEricRafa\Imagens\olhoFechado.png').subsample(17)
        tk.Button(self.root, text="Esconder", image=self.esconder, compound="left", command=self.ocultarSenha, bd=2, relief="raised", font=("Arial", 12, "bold"), bg="#3498db", fg="white").place(relx=0.05, rely=0.49)
    
    def mostrar_nome_bem_vindo(self, nome):
        tk.Label(self.root, text=f"Bem vindo: {nome}", font=("Arial", 14, "bold"), bg="#1e3a56", fg="white").place(relx=0, rely=0.03)
    
    def verificar_login(self):
        user = self.login_user_entry.get()
        password = self.login_password_entry.get()

        if Sq.confirmarLogin(user, password):
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.show_opcoes_frame()
            self.mostrar_nome_bem_vindo(user)
        else:
            messagebox.showerror("Login", "Utilizador ou senha incorretos.")

    def alterar_senha(self):
        user = self.login_user_entry.get()
        confirmar = Sq.obterSenha(user)
        old_password = simpledialog.askstring("Alterar Senha", "Digite a senha atual:")

        if old_password == confirmar:  # Utilizando a função obterSenha para verificar a senha atual
            new_password = simpledialog.askstring("Alterar Senha", "Digite a nova senha:")
            if new_password:
                if Sq.alterarSenha(user, old_password, new_password):
                    messagebox.showinfo("Alterar Senha", "Senha alterada com sucesso!")
                else:
                    messagebox.showerror("Alterar Senha", "Falha ao alterar a senha. Verifique as credenciais.")
        else:
            messagebox.showerror("Alterar Senha", "Senha incorreta. Tente novamente.")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginForm(root)
    
    root.mainloop()
