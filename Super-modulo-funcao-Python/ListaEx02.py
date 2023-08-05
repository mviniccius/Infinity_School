# Crie uma função que recebe um número como argumento e retorna o seu quadrado.
# Exemplo de entrada: 4
# Saída esperada: 16

def square(a: int):   
    return a * a

num1 = int(input('Digite um valor para elevar ao quadrado: '))

print(f"O valor {num1} ao quadrado eh {square(num1)}")
