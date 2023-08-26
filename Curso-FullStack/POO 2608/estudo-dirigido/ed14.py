""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - CRIANDO UMA CLASSE ÚTIL """

# Você se lembra do exemplo do primeiro ed01.py?

nome_pessoa = "Jessé Gomes da Silva Filho" # <class 'str'>
apelido_pessoa = "Zeca Pagodinho"          # <class 'str'>
pessoa_brasileira = True                   # <class 'bool'>
pessoa_carioca = True                      # <class 'bool'>
idade_pessoa = 64                          # <class 'int'>
altura_pessoa = 1.68                       # <class 'float'>
peso_pessoa = 80.0                         # <class 'float'>

# Juntos, faremos um classe, passo a passo, parar guardar o perfil
# do Zeca Pagodinho. Assim, não precisaremos criar um monte de va-
# riáveis soltas, o que deixará nosso código mais organizado.

# 1º PASSO - CRIANDO UMA CLASSE VAZIA CHAMADA 'Perfil'

class Perfil:
    pass

# Note que, toda classe começa com a palavra 'class'. Depois, informamos
# o nome da nossa classe: Perfil. Por padrão, todo nome de classe vem com
# a primeira letra maiúscula: Perfil, Leão, Celular, Computador...
#
# Outra curiosidade é que, se quisermos criar uma classe vazia, sem nada,
# é só escrever a palavra 'pass', de passivo, ou colocar três pontos: ...
# Veja o exemplo da classe Perfil com os três pontos.

class Perfil:
    ...

# E então, qual dos dois você prefere? #TeamPass ou #Team3Pontos?