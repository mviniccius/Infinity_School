# Por enquanto deixaremos nossa função __init__ vazia, colocando pass lá dentro.

""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - CRIANDO UMA CLASSE ÚTIL """

# Precisamos, agora, pedir ao __init_ para "construir" nossa classe. Lembra
# o que o Igor faz? Diz para a classe que o que ela receber de informação
# será de propriedade da classe. Achado não é roubado, não é mesmo?

class Perfil:
    def __init__(self, nome_pessoa, apelido_pessoa, pessoa_brasileira,
                       pessoa_carioca, idade_pessoa, altura_pessoa, peso_pessoa) -> None:
        self.nome_pessoa = nome_pessoa
        self.apelido_pessoa = apelido_pessoa
        self.pessoa_brasileira = pessoa_brasileira
        self.pessoa_carioca = pessoa_carioca
        self.idade_pessoa = idade_pessoa


# Você sentiu falta de alguma(s) coisa(s)? Se sim, complete antes de seguir para o próximo ed.