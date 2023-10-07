import sqlite3 as sql

#variavel de conexao
conexao = sql.connect("bancodedados.db")

#variavel apontador
cursor = conexao.cursor()

#inserir o primeiro cadastro no banco
#cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("Maria", 10))

#consulta ao banco de dados
dados = cursor.execute("SELECT nome, idade FROM pessoas WHERE id = ?", (3,)).fetchall()

print(dados)

#comitando informacao no bando, salvar alteracoes
conexao.commit()
#encerrar conexao com o banco de dados
conexao.close()
