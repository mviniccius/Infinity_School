from pacote.aluno import Aluno

class BancoDeDados:
    def __init__(self, dados: list) -> None:
        self.dados = dados
        
    def mostrar_dados(self) -> None:
        for dado in self.dados:
            print(f"ID: {self.dados.index(dado) + 1}")
            print(f"Nome: {dado.nome_aluno()}")
            print(f"Idade: {dado.idade_aluno()}\n")
            
    def mostrar_dado(self, id: int) -> None:
        print(f"ID: {id}")
        print(f'Nome: {self.dados[id - 1].nome_aluno()}')
        print(f'Idade: {self.dados[id - 1].idade_aluno()}')
        