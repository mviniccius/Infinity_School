# Faça  uma  função  que  recebe  uma  lista  de  números  e  retorna  a  soma  de  todos  os 
# elementos. 
# Exemplo de entrada: [1, 2, 3, 4] 
# Saída esperada: 10

def soma_lista(lista: int):
    soma = 0
    for num in lista:
        soma += num
    return soma
        
lista_num = [8, 15, 1, 4]
print(soma_lista(lista_num))