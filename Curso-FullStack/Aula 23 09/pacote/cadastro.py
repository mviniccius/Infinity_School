class Cadastro:
    def __init__(self, nome: str, idade: int) -> None:
        self.ID = None
        self.nome = nome
        self.idade = idade
    

    def mostrar_cadastro(self) -> None:
        print("Nome:", self.nome)
        print("Idade:", self.idade, end='\n\n')
    

if __name__ == '__main__':

    cadastro1 = Cadastro('Ana Clara', 12)
    cadastro2 = Cadastro('João Pedro', 18)

    cadastro2.mostrar_cadastro()