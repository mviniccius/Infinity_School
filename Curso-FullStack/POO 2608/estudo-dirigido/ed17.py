""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - CRIANDO UMA CLASSE ÚTIL """

# Além do __init__, criaremos outras funções para exibir o seguinte:
#
# >>> O nome, o apelido e a idade da pessoa. Essa função será chamada
#     de info_pessoal();
#
# >>> Se a pessoa é brasileira. Essa função será chamada de brasileira()
#
# >>> Se a pessoa é carioca. Essa função será chamada de carioca()

class Perfil:
    def __init__(self, nome_pessoa, apelido_pessoa, pessoa_brasileira,
                       pessoa_carioca, idade_pessoa, altura_pessoa, peso_pessoa) -> None:
        """
        Explique com suas palavras o que essa função faz aqui neste comentário.
        """
        self.nome_pessoa = nome_pessoa
        self.apelido_pessoa = apelido_pessoa
        self.pessoa_brasileira = pessoa_brasileira
        self.pessoa_carioca = pessoa_carioca
        self.idade_pessoa = idade_pessoa
        self.altura_pessoa = altura_pessoa
        self.peso_pessoa = peso_pessoa
    
    def info_pessoa(self):
        """
        Explique com suas palavras o que essa função faz aqui neste comentário.
        """
        print(f"{self.nome_pessoa}, mais conhecido como {self.apelido_pessoa}, tem {self.idade_pessoa}.")
    
    def brasileiro(self):
        """
        Explique com suas palavras o que essa função faz aqui neste comentário.
        """
        if self.brasileiro == True:
            print(f"{self.nome_pessoa} é brasileira.")
        else:
            print(f"{self.nome_pessoa} não é brasileira.")
    
    def carioca(self):
        """
        Explique com suas palavras o que essa função faz aqui neste comentário.
        """
        if self.brasileiro == True:
            print(f"{self.nome_pessoa} é cariosa.")
        else:
            print(f"{self.nome_pessoa} não é carioca.")