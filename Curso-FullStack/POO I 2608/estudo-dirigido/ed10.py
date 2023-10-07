""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - VOCÊ SE LEMBRA DO IGOR? """

# Você se lembra do Igor, do ed07.py? Então, agora nós vamos conhecê-lo
# um pouco mais, entendendo o que é que ele está fazendo na classe.
#
# Bom até então, nós criamos algumas classes, certo? Leao, Cachorro,
# Computador, Celular... Além disso, colocamos funções dentro delas,
# afinal, um Computador, por exemplo, pode calcular() ou renderizar().
# Fizemos o mesmo para o Cachorro:



class Cachorro:
    def __init__(self) -> None:
        ...

    def latir(self):
        print("Au au... au au...")

    def beber_agua(self):
        print("Blof, blof, blof...")

    def uivar(self):
        print("Auuu... auuu")



# No entanto, faltou pensar uma coisinha sobre cachorro: quais as
# suas características? Qual a cor do pelo? Qual o tamanho? Qual a
# raça? Qual o tamanho do pelo?
#
# Essas características, ou ATRIBUTOS, fazem parte do nosso Cachor-
# ro e, por isso, precisamos informar à nossa classe. Dessa forma,
# toda vez que um cachorro for "criado" nós informaremos as carac-
# terísticas do animal, por exemplo:
#
#
#
# >>> André: O meu cachorro é preto, médio porte, vira-lata, pelo curto.
#            E o seu, Natã?
# >>> Natã: O meu é caramelo, vira-lata também, bem grande e pelo curto.
# <<< Otto: O meu é o mais bonito de todos... É um basset francês, pelo
#           curto, pequeno, cor branca com bege e se chama Pierre... O
#           animal de vocês não tem nome?
# >>> Natã: o meu se chama Gato...
# >>> André: o meu Beiçola, e adora pastel.
#
#
#
# Perceba que, ao longo do diálogo entre André, Natã e Otto, surgiu uma
# nova característica para o cachorro: o nome. Além disso, note que, apesar
# dos cães serem cães eles eram diferentes quanto às suas características.
# Em POO, chamamos essas características de ATRIBUTOS. Assim, a partir da
# classe Cachorro, podemos criar cães diferentes, mudando apenas os atributos
# do novo cachorro que estamos criando:
#
# >>> NOVO CACHORRO:
#     >>> nome: batata,
#     >>> raça: basset,
#     >>> tamanho: pequeno,
#     >>> cor: azul da cor do mar,
#     >>> pelo longo: azul da cor do mar
#
# Quais outras características você consegue pensar para um cachorro?
# Resposta: 