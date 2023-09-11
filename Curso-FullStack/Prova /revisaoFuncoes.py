#Escreva uma função em Python que recebe uma lista de números inteiros e retorna a média aritmética dos valores.

def media_lista(lista: list) -> float:
    soma = 0
    denominador = len(lista)

    for num in lista:
        soma = soma + num
    
    media = soma / denominador

    return media

#testando

lista = [2, 2, 2, 2, 2, 2, 2]
print(f"A media da lista eh: {media_lista(lista)}")
