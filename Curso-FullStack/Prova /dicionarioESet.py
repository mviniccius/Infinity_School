#c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade.

def maior_idade(dicionario):
    pessoa_mais_velha = None
    idade_mais_velha = 0

    for nome, idade in dicionario.items(): #funcao items retorna a chave-valor do dicionario
        if idade > idade_mais_velha:
            pessoa_mais_velha = nome
            idade_mais_velha = idade
    return pessoa_mais_velha



#Trazendo o dicionario:
pessoas = {

    "João": 23,

    "Maria": 28,

    "Pedro": 35,

    "Lucas": 19

}
#Resposta:
#A
#Acesse a idade da pessoa "João" e armazene em uma variável chamada idade_joao.

idade_joao= pessoas["João"]
print(idade_joao)

#B
#Adicione uma nova pessoa ao dicionário com nome "Ana" e idade 31.

pessoas["Ana"] = 31
#conferir se foi adicionado corretamente
print(pessoas)

#c) Crie uma função chamada maior_idade que recebe um dicionário como argumento e retorna o nome da pessoa com a maior idade.
nome_mais_velho = maior_idade(pessoas)
print(f"A pessoa mais velha eh: {nome_mais_velho}")
