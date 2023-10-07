""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - PONTOS IMPORTANTES """

# Antes de compreendermos mais sobre CLASSES, precisamos entender
# sobre a ideia de Orientação a Objetos. Afinal, o que isso quer
# dizer no contexto de programação em Python?
#
# OBJETIVOS da Programação Orientada a Objetos (POO):
#
# >>> possibilitar que sejam construídos programas maiores e mais robustos (robutez)
# >>> possibilitar que o sistema funcione em diferentes ambientes (adaptabilidade)
# >>> possibilitar que o código do sistema seja reutilizado em outros sistemas (reusabilidade)
#
# A POO possui alguns PRINCÍPIOS FUNDAMENTAIS para sua implementação:
#
# >>> é possível criar "coisas" do mundo real em código (abstração)
# >>> é possível evitar a repetição de código passando os comando "de pai para filho" (herança)
# >>> é possível garantir maior segurança aos dados/valores manipulados (encapsulamento)
# >>> é possível trabalhar de formas diferentes com o mesmo código (polimorfismo)
# 
# Veja o exemplo abaixo:





class Cachorro:
    def __init__(self) -> None:
        """
            Oii, meu nome é Igor! Ninguém entende muito bem o que estou fazendo aqui,
            mas seremos melhor apresentados ao longo do curso, tá? Até mais ;)
        """
        ...


    def latir(self):
        """
            Olá, meu nome é Lauro, e eu faço o cachorro latir     >:(
        """
        print("Au au... au au...")
    

    def beber_agua(self):
        """
            Olá, meu nome é Bárbara, e eu faço o cachorro ficar sempre hidratado      :3
        """
        print("Blof, blof, blof...")
    

    def uivar(self):
        """
            Olá, meu nome é Ubaldo, e eu faço o cachorro uivarr a aUUUUU...     :u
        """
        print("Auuu... auuu")





# No exemplo acima, criamos uma classe Cachorro. O que é possível fazer com a classe cachorro?
# Resposta:
#
# Qual dos PRINCÍPIOS FUNDAMENTAIS da POO se aplicaria ao exemplo da classe Cachorro?
# Resposta: 
#
# Você pode se perguntar: OK, criei uma classe Cachorro, mas e agora? O que eu faço com isso?
# Em orientação a objeto, nós podemos chamar uma classe para usá-la em outro contexto:

novo_cachorro1 = Cachorro()  # chamamos a classe Cachorro para criar um cachorro 1

novo_cachorro1.latir()
novo_cachorro1.beber_agua()
novo_cachorro1.uivar()

# No exemplo acima, definimos uma variável 'novo_cachorro1':
# >>> novo_cachorro1 = Cachorro()
# 
# Isso que dizer que "criamos" um novo cachorro a partir da classe definida anteriormente.
# Seguindo essa lógica, poderíamos criar mais cachorros:

novo_cachorro2 = Cachorro() # chamamos a classe Cachorro para criar um cachorro 2
novo_cachorro3 = Cachorro() # chamamos a classe Cachorro para criar um cachorro 3
novo_cachorro4 = Cachorro() # chamamos a classe Cachorro para criar um cachorro 3

# Veja que, ao criamos um novo cachorro, tudo o que foi definido na classe Cachorro foi
# automaticamente atribuído à variável. Assim, podemos utilizar as funções latir(),
# beber_agua() ou uivar():

novo_cachorro2.latir()          # o cachorro 2 está latindo...
novo_cachorro3.beber_agua()     # o cachorro 3 está bebendo água...
novo_cachorro4.uivar()          # o cachorro 4 está uivando...

# >>> André: mas professor, qual a utilidade de criar um cachorro no Python?
# >>> Professor: ... (cri, cri, cri...)

# Pois é, desenvolvedores... Pode parecer maluco isso, mas vamos desvendar
# esse universo mais afrente, beleza? Confia que o pai tá on!