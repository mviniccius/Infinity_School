# Escreva uma função que recebe um número e verifica se é par. 
# Exemplo de entrada: 6 
# Saída esperada: True

def verifca_par(a):
    return True if a % 2 == 0 else False

#Aqui o main
num = int(input("Digite um valor para virificar se eh par: "))
print(verifca_par(num))
