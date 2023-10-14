#Classe jogador onde sera criado o objeto jogador

class Jogadores:
    def __init__(self, nome: str, nome_do_time: str, numero_camisa: int) -> None:
        self.nome = nome
        self.nome_do_time = nome_do_time
        self.numero_camisa = numero_camisa

    def dados_jogador(self) -> None:
        print(f"Nome do jogador: {self.nome}")
        print(f"Time atual: {self.nome_do_time}")
        print(f"Numero da camisa: {self.numero_camisa}")