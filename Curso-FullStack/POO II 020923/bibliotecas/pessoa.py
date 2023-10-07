class Pessoa: # ex01
    def __init__(self, nome, sobrenome: str, idade: int, naturalidade: str, nacionalidade: str, data_nascimento: str, numero_id: str, filiacao: list) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade
        self.data_nascimento = data_nascimento
        self.numero_id = numero_id
        self.filiacao = filiacao
             
        
    def certidao_nascimento(self) -> None:
        print(f"Nome:{self.nome}")
        print(f"Sobrenome:{self.sobrenome}")
        print(f"Idade:{self.idade}")
        print(f"Naturalidade:{self.naturalidade}")
        print(f"Nacionalidade:{self.nacionalidade}")
        print(f"Data Nascimento:{self.data_nascimento}")
        print(f"Identidade:{self.numero_id}")
        print(f"Filiacao\nPai: {self.filiacao[0]}\nMãe: {self.filiacao[1]}")
       
     