# Crie uma função que recebe uma lista de números e retorna o maior valor. 
# Exemplo de entrada: [3, 8, 2, 5] 
# Saída esperada: 8

def acha_maior(lista: list):
    maior = -9999999
    for i in lista:
        if i > maior:
            maior = i
    return maior

#Aqui o main
lista_num = [8, 15, 23, 4]
print(acha_maior(lista_num))
