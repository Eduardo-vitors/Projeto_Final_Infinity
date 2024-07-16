# Programação De um sistema de controle de acesso para Empresa Wayne Enterprises
#Autor: EDUARDO VITOR (KEDU)
#JULHO 2024

#Biblioteca do Banco de dados
import sqlite3

# Classe principal que gerencia o sistema de segurança
class SistemaDeGerenciamento:
    # Função para criar o banco de dados e suas tabelas
    def criar_banco_de_dados():
        conexao = sqlite3.connect('seguranca.db')
        cursor = conexao.cursor()

        # Tabela 'usuarios' para armazenar informações sobre os usuários
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
        ''')

        # Tabela 'recursos' para armazenar informações sobre os recursos
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
        ''')
        #Feito para criar exemplos para teste eles ainda estão no Banco de Dados.
        cursor.execute (" INSERT INTO usuarios (id, nome,senha,tipo) VALUES (1, 'Bruce','Batman','admin'),(2, 'Clark','Superhomen','funcionario'),(3, 'Du','desenho','gerente')")
        cursor.execute (" INSERT INTO recursos (id, nome,tipo) VALUES (1, 'Câmera de Segurança', 'equipamento')")
        conexao.commit()

    
        conexao.close()
    criar_banco_de_dados()

    def __init__(self):
        self.db_name = 'seguranca.db'

    # Método para adicionar usuário ao banco de dados
    def adicionar_usuario(self, nome,senha,tipo):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO usuarios (nome, senha, tipo) VALUES (?,?,?)', (nome,senha,tipo))
        conexao.commit()
        conexao.close()

    # Método para adicionar recurso ao banco de dados
    def adicionar_recurso(self, nome, tipo):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO recursos (nome, tipo) VALUES (?, ?)', (nome, tipo))
        conexao.commit()
        conexao.close()

    # Método para listar funcionário do banco de dados e retorna o (id,nome,senha,tipo) para o app.py que aparecerá numa tabela
    def listar_funcionario(self):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome,senha,tipo FROM usuarios')
        rows1 = cursor.fetchall()
        conexao.close()
        return rows1
    
    # Método para listar recursos do banco de dados e retorna o (id,nome,tipo) para o app.py que aparecerá numa tabela
    def listar_recursos(self):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('SELECT id, nome, tipo FROM recursos')
        rows2 = cursor.fetchall()
        conexao.close()
        return rows2

    # Método para autenticar usuário no sistema, verificação se usuário existe ou não e retorna o tipo de usuário para usar a verificação no app.py para proibir acesso em algumas partes do sistema.
    def autenticar_usuario(self, usuario_senha, nome):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('SELECT tipo FROM usuarios WHERE senha = ? AND nome = ?', (usuario_senha, nome))
        row = cursor.fetchone()
        conexao.close()
        if row:
            return row[0]
        return None

    # Método para atualizar informações de um recurso do Banco de Dados
    def atualizar_recurso(self, id_recurso, nome, tipo):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('UPDATE recursos SET nome = ?, tipo = ? WHERE id = ?', (nome, tipo, id_recurso))
        conexao.commit()
        conexao.close()

    # Método para remover um recurso do banco de dados
    def remover_recurso(self, id_recurso):
        conexao = sqlite3.connect(self.db_name)
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM recursos WHERE id = ?', (id_recurso,))
        conexao.commit()
        conexao.close()
