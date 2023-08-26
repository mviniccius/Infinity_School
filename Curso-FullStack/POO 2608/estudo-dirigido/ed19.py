""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - CRIANDO O NOSSO PERFIL """

# Pronto! Classe criada e ponta para ser utilizada. Vamos lá?

class Perfil:
    def __init__(self, nome_pessoa, apelido_pessoa, pessoa_brasileira,
                       pessoa_carioca, idade_pessoa, altura_pessoa, peso_pessoa) -> None:
        """
        Este método constrói a classe para que tudo funcione corretamente.
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
        Este método exibe as informações básicas da pessoa.
        """
        print(f"{self.nome_pessoa}, mais conhecido como {self.apelido_pessoa}, tem {self.idade_pessoa}.")
    
    def brasileiro(self):
        """
        Este método exibe se a pessoa é brasileira ou não.
        """
        if self.brasileiro == True:
            print(f"{self.nome_pessoa} é brasileira.")
        else:
            print(f"{self.nome_pessoa} não é brasileira.")
    
    def carioca(self):
        """
        Este método exibe se a pessoa é carioca ou não.
        """
        if self.brasileiro == True:
            print(f"{self.nome_pessoa} é cariosa.")
        else:
            print(f"{self.nome_pessoa} não é carioca.")
    
    def perfil_completo(self):
        """
        Este método exibe o perfil completo da pessoal.
        """
        print(f"Perfil :: {self.nome_pessoa}")
        
        print(f"Nome completo: {self.nome_pessoa}")
        print(f"Apelido/Nome Artístico: {self.apelido_pessoa}")
        print(f"Naturalidade: {self.carioca}")
        print(f"Nacionalidade: {self.brasileiro}")
        print(f"Idade: {self.idade_pessoa}")
        print(f"Altura e Peso: {self.altura_pessoa} cm e {self.peso_pessoa} kg")
        
        print(f"Perfil :: {self.nome_pessoa}")


# CRIANDO UMA CÓPIA DA NOSSA CLASSE PARA CRIAR O PERFIL DO ZECA PAGODINHO

perfil1 = Perfil(nome_pessoa="Jessé Gomes da Silva Filho",
                 apelido_pessoa="Zeca Pagodinho",
                 pessoa_brasileira=True,
                 pessoa_carioca=True,
                 idade_pessoa=64,
                 altura_pessoa=1.68,
                 peso_pessoa=80.0)

perfil1.info_pessoa()

# Agora, teste as outras funções da nossa classe:
#
# >>> .brasileiro()
# >>> .carioca()
# >>> .perfil_completo()