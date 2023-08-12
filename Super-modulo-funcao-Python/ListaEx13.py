# Escreva uma função que recebe uma lista de números e retorna a mediana. 
# Exemplo de entrada: [1, 2, 3, 4, 5] 
# Saída esperada: 3 

def mediana(numeros: list) -> int:
    tamanho = len(numeros)/2
    tamanho = int(tamanho)
    numero = numeros[tamanho]
    return numero

#main
lista_num = [1, 2, 3, 4, 5, 9, 10]
print(mediana(lista_num))
