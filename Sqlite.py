import sqlite3

conn = sqlite3.connect('baseDados.db')
cur = conn.cursor()

def confirmarLogin(user, passw):
    conn = sqlite3.connect('baseDados.db')
    cur.execute("SELECT Id FROM user WHERE Nome=? AND Pin=?", (user, passw))
    result = cur.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False

def criarConta(user, passw):
    conn = sqlite3.connect('baseDados.db')
    cur.execute("INSERT INTO user (Nome, Pin) VALUES (?, ?)", (user, passw))
    conn.commit()
    conn.close()
    
def alterarSenha(user, old_password, new_password):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()  # Adicionar esta linha para criar o cursor
    cur.execute("SELECT Id FROM user WHERE Nome=? AND Pin=?", (user, old_password))
    result = cur.fetchone()
    print("DEBUG: Resultado da consulta:", result)
    if result:
        cur.execute("UPDATE user SET Pin=? WHERE Nome=?", (new_password, user))
        conn.commit()
        conn.close()
        print("DEBUG: Senha alterada com sucesso.")
        return True
    else:
        conn.close()  # Certifique-se de fechar a conexão mesmo em caso de falha
        print("DEBUG: Falha ao alterar a senha. Usuário ou senha incorretos.")
        return False


def obterSenha(user):
    conn = sqlite3.connect('baseDados.db')
    cur = conn.cursor()  # Adicione esta linha para criar o cursor
    cur.execute("SELECT Pin FROM user WHERE Nome=?", (user,))  # Note a vírgula após (user,)
    result = cur.fetchone()
    conn.close()
    if result:
        return result[0]  # Retorna apenas o primeiro elemento da tupla (a senha)
    else:
        return None
