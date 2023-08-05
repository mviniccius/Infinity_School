# Crie uma função que recebe uma string e retorna a mesma string invertida. 
# Exemplo de entrada: "python" 
# Saída esperada: "nohtyp"

def inverte_palavra(palavra: str):
    palavra_invertida = ""
   
    for letra in palavra[::-1]:
        palavra_invertida = palavra_invertida + letra
    
    return palavra_invertida        
#main
texto = "python"
print(inverte_palavra(texto))