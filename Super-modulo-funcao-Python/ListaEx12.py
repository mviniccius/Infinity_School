# Faça uma função que recebe uma lista de números e retorna a média deles. 
# Exemplo de entrada: [4, 5, 6, 7] 
# Saída esperada: 5.5

def calcula_media(numeros: list) -> float:
    quantidade = len(numeros)
    soma = 0        #variavel para acumular os valores
    for i in numeros:
        soma +=i
    
    media = soma / quantidade
    return media
#main
lista_num = [8, 15, 23, 4]
print(calcula_media(lista_num))
