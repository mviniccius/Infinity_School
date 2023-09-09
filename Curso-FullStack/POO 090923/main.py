from pacote.bd import BancoDeDados as DB
from dados import lista_alunos as dados

db = DB(dados)

db.mostrar_dado(id=1)
db.mostrar_dados()
