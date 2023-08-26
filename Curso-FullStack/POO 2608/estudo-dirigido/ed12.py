""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - VOCÊ SE LEMBRA DO IGOR? """

# >>> Igor: Oiê, como vai? Sou eu de novo, o Igor...
# >>> Igor: Na verdade, Igor é apelido, né, pois meu nome é Init.
# >>> Igor: Assim... quer dizer... meu nome é Initialization Jr.. Meu pai é Inglês,
#           e me "presenteou" com esse nome um pouco curioso, haha...
# >>> Igor: Bom, eu vim aqui para te mostrar que, apesar de um nome bem difícil, eu
#           faço uma coisa muito simples: defino as características da sua classe e
#           inicializo todas elas para que funcionem direitinho =3
# >>>       Veja só como eu faço isso...



class Cachorro:
    def __init__(self, nome: str, raca: str, cor: str, pelo: str, idade: str, tem_dono: bool) -> None:
        self.nome = nome
        self.raca = raca
        self.cor  = cor
        self.pelo = pelo
        self.idade = idade
        self.tem_dono = tem_dono

    def latir(self):
        print("Au au... au au...")

    def beber_agua(self):
        print("Blof, blof, blof...")

    def uivar(self):
        print("Auuu... auuu")



# >>> Igor: Tipo, o que eu fiz foi o seguinte: eu falei para a sua classe que o que ela receber como
#           característica do cachorro será a sua própria características. Por isso aquela palavrinha
#           self, sabe? Quer dizer que tudo o que está dentro da classe é dela agora. Afinal, achado
#           não é roubado, hihi :3
#
# >>> Igor: Aí, o que ela receber como 'nome' será o próprio nome, e assim por diante... Difícil?
#           Se você estiver confuso, vamos resolver isso já já... Mas, primeiro, o que aconteceu
#           quando você tentou executar o código do ed11.py? Deu certo?
# >>> Igor: Provavelmente, não!!! ;) Eu não deixo as coisas funcionarem até que me informem o que
#           eu preciso. Por isso, se você quiser criar um cachorro agora, tem que fazer assim:

cachorro1 = Cachorro('Wilson', 'vira-latas', 'alcione', 'longo',     3,       False)
#                      nome        raça         cor       pelo     idade     tem dono?

# >>> Igor: Agora está tudo certo. Eu faço o meu trabalho e você o seu =).
# >>> Igor: Se precisar de alguma coisa é só chamar, beleza?