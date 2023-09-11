 #a) Implemente a função com o nome "maior_numero" e utilizando condicionais.

def maior_numero(num1: int, num2: int) -> int:
    if num1 > num2:
        return num1
    else:
        return num2

#b) Implemente a mesma função, porém utilizando a função "max".

def maior_numero2(num1, num2):
    return max(num1, num2)

#testando

a = 5
b = 3
print(f"O maior numero da funcao:{maior_numero(a, b)}")
print(f"O maior numero da funcao:{maior_numero2(a, b)}")
