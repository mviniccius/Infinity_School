import sqlite3 as sql

conexao = sql.connect("padaria.db")

cursor = conexao.cursor()

cursor.execute("INSERT INTO clientes(cliente) VALUES(?)", ("Roger",))

conexao.commit()
conexao.close()