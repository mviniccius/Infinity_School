# Escreva uma função que recebe uma lista de palavras e retorna quantas delas têm mais 
# de 5 caracteres. 
# Exemplo de entrada: ["python", "programação", "é", "divertida"] 
# Saída esperada: 3

def conta_caracteres(palavras: list):
    quantidade_palavras = len(palavras)
    count = 0
    
    for i in range(0, quantidade_palavras):
        if len(palavras[i]) > 5:
            count += 1
    return count

#Main
frase = ["python", "programação", "é", "divertida"]
print(conta_caracteres(frase))