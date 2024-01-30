import sqlite3

conn = sqlite3.connect('baseDados.db')
cur = conn.cursor()

def confirmarLogin(user, passw):
    cur.execute("SELECT Id FROM user WHERE Nome=:user AND Pin=:passw")
    result = cur.fetchone()
    if result:
        # Usuário e senha correspondem
        return True
    else:
        # Usuário ou senha incorretos
        return False