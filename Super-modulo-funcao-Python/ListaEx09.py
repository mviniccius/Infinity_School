# Faça uma função que recebe uma lista de números e retorna uma nova lista com apenas 
# os números ímpares. 
# Exemplo de entrada: [1, 2, 3, 4, 5, 6] 
# Saída esperada: [1, 3, 5]

def escolhe_impar(lista: list):
    lista_impar = []
    
    for num in lista:
        if num % 2 != 0:
            lista_impar.append(num)
    return lista_impar

#Aqui o main
lista_num = [8, 15, 23, 4]
print(escolhe_impar(lista_num))