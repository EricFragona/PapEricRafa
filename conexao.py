import sqlite3

def criar_conexao():
    conexao = sqlite3.connect('database.db')
    return conexao


def inserir_usuario(conexao, username, password):
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO usuarios (username, password)VALUES (?, ?)''', (username, password))
    conexao.commit()

def buscar_usuario(conexao, username, password):
    cursor = conexao.cursor()
    cursor.execute('''
        SELECT * FROM usuarios
        WHERE username = ? AND password = ?
    ''', (username, password))
    usuario = cursor.fetchone()
    return usuario
