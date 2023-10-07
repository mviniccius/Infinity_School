""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - CRIANDO UMA CLASSE ÚTIL """

# Agora que criamos nossa classe, criaremos o primeiro método: o Igor,
# você se lembra dele? Além disso, passaremos para o Igor, ou init, as
# seguintes informações como parâmetros:
#
# >>> nome_pessoa: str
# >>> apelido_pessoa: str
# >>> pessoa_brasileira: str
# >>> pessoa_carioca: str
# >>> idade_peessoa: int
# >>> altura_pessoa: float
# >>> peso_pessoa: float
# 
# Façamos juntos:

class Perfil:
    def __init__(self, nome_pessoa, apelido_pessoa, pessoa_brasileira,
                       pessoa_carioca, idade_pessoa, altura_pessoa, peso_pessoa) -> None:
        pass

# Por enquanto deixaremos nossa função __init__ vazia, colocando pass lá dentro.