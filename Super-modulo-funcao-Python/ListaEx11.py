# Crie uma função que recebe uma string e retorna a mesma string invertida. 
# Exemplo de entrada: "python" 
# Saída esperada: "nohtyp"

def inverte_palavra(palavra: str):
    palavra_invertida = ""
    tamanho = len(palavra) -1
    while tamanho != -1:
        palavra_invertida += palavra[tamanho]
        tamanho -= 1
    
    return palavra_invertida        
#main
texto = "python"
print(inverte_palavra(texto))