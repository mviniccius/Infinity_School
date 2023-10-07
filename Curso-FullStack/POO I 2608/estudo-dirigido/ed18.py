""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - CRIANDO UMA CLASSE ÚTIL """

# Finalmente, criaremos mais uma função, chamada perfil_completo() que exibirá
# todas as informações da pessoa da seguinte maneira:
#
# <<< Perfil :: Jessé Gomes da Silva Filho >>>
#
# Nome completo: Jessé Gomes da Silva Filho
# Apelido/Nome Artístico: Zeca Pagodinho
# Naturalidade: Carioca
# Nacionalidade: Brasileiro
# Idade: 64 anos
# Altura e Peso: 1,68 cm e 80 kg
# 
# <<< Perfil :: Jessé Gomes da Silva Filho >>>

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
    
    def perfil_completo(self):
        """
        Explique com suas palavras o que essa função faz aqui neste comentário.
        """
        print(f"Perfil :: {self.nome_pessoa}")
        
        print(f"Nome completo: {}")
        print(f"Apelido/Nome Artístico: {}")
        print(f"Naturalidade: {}")
        print(f"Nacionalidade: {}")
        print(f"Idade: {}")
        print(f"Altura e Peso: {} cm e {} kg")
        
        print(f"Perfil :: {self.nome_pessoa}")

# Antes de seguir para o próximo ed, lembre-se de completar as informações da
# função perfil_completo(). Como exibir o nome da pessoa? E a idade?
    