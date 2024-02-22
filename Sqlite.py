import sqlite3

def confirmarLogin(user, passw):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()
    cur.execute("SELECT Id FROM user WHERE Nome=? AND Pin=?", (user, passw))
    result = cur.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def criarConta(user, passw):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO user (Nome, Pin) VALUES (?, ?)", (user, passw))
    cur.execute("INSERT INTO permissoes (Perms, Comentario) VALUES (?, ?)", (1, "player"))
    cur.execute("INSERT INTO progresso (Moedas) VALUES (?)", (0,))
    cur.execute("INSERT INTO upgrades (Upg1, Upg2, Upg3, Upg4 ,Upg5) VALUES (?, ?, ?, ?, ?)", (0, 0, 0, 0, 0))
    conn.commit()
    conn.close()

    
def alterarSenha(user, old_password, new_password):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()
    cur.execute("SELECT Id FROM user WHERE Nome=? AND Pin=?", (user, old_password))
    result = cur.fetchone()
    if result:
        cur.execute("UPDATE user SET Pin=? WHERE Nome=?", (new_password, user))
        conn.commit()
        conn.close()
        return True
    else:
        conn.close()
        return False

def obterSenha(user):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()
    cur.execute("SELECT Pin FROM user WHERE Nome=?", (user,))
    result = cur.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return None
    
def apagarConta(user):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE Nome=?", (user,))
    existing_user = cur.fetchone()
    print("Existing User:", existing_user)
    if not existing_user:
        conn.close()
        return False
    cur.execute("DELETE FROM user WHERE Nome=?", (user,))
    conn.commit()
    conn.close()
    return True

def alterarNome(user, novo_nome):
    try:
        conn = sqlite3.connect('baseDados.db')
        cur = conn.cursor()
        cur.execute("UPDATE user SET Nome = ? WHERE Nome = ?", (novo_nome, user))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("Error:", e)
        return False
