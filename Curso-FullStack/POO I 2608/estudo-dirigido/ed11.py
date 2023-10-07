""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - VOCÊ SE LEMBRA DO IGOR? """

# Definindo as características (ATRIBUTOS) da classe cachorro.



class Cachorro:
    def __init__(self, nome: str, raca: str, cor: str, pelo: str, idade: str, tem_dono: bool) -> None:
        ...

    def latir(self):
        print("Au au... au au...")

    def beber_agua(self):
        print("Blof, blof, blof...")

    def uivar(self):
        print("Auuu... auuu")



# Execute o código abaixo e faça comentários sobre a saída de dados (mensagem no terminal):

cachorro1 = Cachorro()

# O que aconteceu após a execução do código? Comente com seus colegas antes de responder.
# Resposta: 