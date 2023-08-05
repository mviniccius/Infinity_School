# Crie uma função que recebe uma lista de números e retorna uma nova lista com apenas 
# os números pares. 
# Exemplo de entrada: [1, 2, 3, 4, 5, 6] 
# Saída esperada: [2, 4, 6]  

def escolhe_par(lista: list):
    lista_par = []
    
    for num in lista:
        if num % 2 == 0:
            lista_par.append(num)
    return lista_par

#Aqui o main
lista_num = [8, 15, 23, 4]
print(escolhe_par(lista_num))