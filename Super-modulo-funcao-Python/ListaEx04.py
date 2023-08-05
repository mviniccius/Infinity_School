# Escreva uma função que recebe uma lista de strings e retorna a concatenação de todas 
# elas. 
# Exemplo de entrada: ["Olá", "mundo", "!"] 
# Saída esperada: "Olá mundo!"


def concatena_string(frase: list):#nao tratado se tem acentuacao no final da frase!
    string = ""
    for palavra in frase:
        string += palavra        
        string += " "        
    return string

lista_string = ["Ola", "mundo", "!"]
print(concatena_string(lista_string))
