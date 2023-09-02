from bibliotecas.pessoa import Pessoa

class Funcionario(Pessoa): # ex02
    def __init__(self,
                 nome: str, 
                 sobrenome: str,
                 idade: int,
                 naturalidade: str,
                 nacionalidade: str,
                 data_nascimento: str,
                 numero_id: str,
                 filiacao: list,
                 cargo:str,
                 setor: str,
                 data_contratacao: str,
                 salario: float) -> None:
        
        
        super().__init__(nome, sobrenome, idade, naturalidade, nacionalidade, data_nascimento, numero_id, filiacao)
        self.cargo = cargo
        self.setor = setor
        self.data_contratacao = data_contratacao
        self.salario = salario
        
    def cracha_funcionario(self) -> None:
        print(f"Nome: {self.nome} {self.sobrenome}")
        print(f"Cargo: {self.cargo}")
        print(f"Setor: {self.setor}")