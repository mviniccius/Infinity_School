from pacote.bd import BancoDeDados as DB
from pacote.aluno import Aluno
from dados import lista_alunos as dados

db = DB(dados)

db.adicionar_dado('Jupira', 15)
db.adicionar_dado1(Aluno('Ostrogeno', 80))
db.mostrar_dados()
