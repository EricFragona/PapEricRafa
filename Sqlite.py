import sqlite3

conn = sqlite3.connect('baseDados.db')
cur = conn.cursor()

def confirmarLogin(user, passw):
    cur.execute("SELECT Id FROM user WHERE Nome=? AND Pin=?", (user, passw))
    result = cur.fetchone()
    if result:
        return True
    else:
        return False

def criarConta(user, passw):
    cur.execute("INSERT INTO user (Nome, Pin) VALUES (?, ?)", (user, passw))
    conn.commit()
    
def alterarSenha(user, old_password, new_password):
    cur.execute("SELECT Id FROM user WHERE Nome=? AND Pin=?", (user, old_password))
    result = cur.fetchone()

    if result:
        cur.execute("UPDATE user SET Pin=? WHERE Nome=?", (new_password, user))
        conn.commit()
        return True
    else:
        return False