import sqlite3 as sql

#conecta ao banco de dados
conexao = sql.connect('banco.db')

#cursor para registros
cursor = conexao.cursor()

#executa o comando sql
cursor.execute("INSERT INTO produtos(nome, qntd, valor) VALUES(?, ?, ?)", ('Liquidificador', 10, 120))

#salva informacoes no banco
conexao.commit()

#Encerra conexão
conexao.close()