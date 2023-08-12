# Crie uma função que recebe um número e verifica se é primo. 
# Exemplo de entrada: 7 
# Saída esperada: True

def verifica_primo(num: int) -> bool:
    if num <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    # Percorre os números de 2 até a raiz quadrada do número
    for i in range(2, int(num ** 0.5) + 1):
        # Verifica se o número é divisível por i
        if num % i == 0:
            return False  # Se for divisível, não é primo

    return True  # Se não foi divisível por nenhum número, é primo

#main
numero = int(input("Digite um numero para verificar se eh primo: "))
print(verifica_primo(numero))