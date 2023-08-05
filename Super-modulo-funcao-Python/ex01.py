#Estrututa Sequencial de funcao

def saudacao(nome: str, idade: int): #na declaracao de parametro eh possivel colocar o tipo de dado esperado

    print(f"seja bem vindo ao curso {nome}")
    print(f'voce tem {idade} anos!')
    
nome = input('Digite seu nome: ')
idade = int(input("Digite sua idade"))
saudacao(nome, idade) #chamada da funcao somente depois da declaracao da funcao
