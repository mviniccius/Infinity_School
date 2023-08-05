# Faça uma função que recebe uma lista de números e retorna o menor valor. 
# Exemplo de entrada: [3, 8, 2, 5] 
# Saída esperada: 2

def acha_menor(lista: list):
    menor = 9999999
    for i in lista:
        if i < menor:
            menor = i
    return menor

#Aqui o main
lista_num = [8, 15, 23, 4]
print(acha_menor(lista_num))
