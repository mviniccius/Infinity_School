#Aula dia 12/08
def imprime_borda():
    print("################")

##################################################################################

#Faça uma função que retorne True se o número informado como argumento for é par.
def validacao(numero: int) -> bool:     #tradicional
    if numero % 2 == 0:
        return True
    else:
        return False

def validacao2(numero: int) -> bool:    #Operador Ternario
    return True if numero % 2 == 0 else False

validacao3 = lambda numero : True if numero % 2 == 0 else False

imprime_borda()
print("Exercicio 1")
print(validacao(4))
print(validacao2(3))
print(validacao3(4))
imprime_borda()

##################################################################################

#Faça uma função que retorne True se o número informado como argumento for menor que zero.
def numero_negativo(numero: int) -> bool:   #Tradicional
    if numero < 0:
        return True
    else:
        return False

def numero_negativo2(numero: int) -> bool:  #ternario
    return True if numero < 0 else False

numero_negativo3 = lambda numero : True if numero < 0 else False

imprime_borda()
print("Exercicio 2")
print(numero_negativo(5))
print(numero_negativo2(-5))
print(numero_negativo3(5))
imprime_borda()

#Faça uma função que retorne True se o número informado como argumento for maior que zero
def numero_positivo(numero: int) -> bool:   #Tradicional
    if numero > 0:
        return True
    else:
        return False
    
def numero_positivo2(numero: int) -> bool:  #ternario
    return True if numero > 0 else False

numero_positivo3 = lambda numero : True if numero > 0 else False

imprime_borda()
print("Exercicio 3")
print(numero_positivo(5))
print(numero_positivo2(-5))
print(numero_positivo3(5))
imprime_borda()

##################################################################################

#Faça uma função que retorne True se o número informado como argumento for igual que zero.

def numero_zero(numero: int) -> bool:   #Tradicional
    if numero == 0:
        return True
    else:
        return False
def numero_zero2(numero: int) -> bool:  #ternario
    return True if numero == 0 else False

numero_zero3 = lambda numero : True if numero == 0 else False

imprime_borda()
print("Exercicio 4")
print(numero_zero(0))
print(numero_zero2(5))
print(numero_zero3(3))
imprime_borda()

##################################################################################

#Faça uma função que retorne True se o número informado como argumento for múltiplo de 2.

def multiplo_dois(numero: int) -> bool:     #Tradicional
    if numero % 2 == 0:
        return True
    else:
        return False

def multiplo_dois2(numero: int) -> bool:    #ternario
    return True if numero % 2 == 0 else False

multiplo_dois3 = lambda numero : True if numero % 2 == 0 else False

imprime_borda()
print("Exercicio 5")
print(multiplo_dois(4))
print(multiplo_dois2(5))
print(multiplo_dois3(6))
imprime_borda()

##################################################################################

#Faça uma função que retorne True se o número informado como argumento for múltiplo de 3.

def multiplo_tres(numero: int) -> bool: # tradicional
    if numero % 3 == 0:
        return True
    else:
        return False

def multiplo_tres2(numero: int) -> bool: #ternario
    return True if numero % 3 == 0 else False

multiplo_tres3 = lambda numero : True if numero % 3 == 0 else False

imprime_borda()
print("Exercicio 6")
print(multiplo_tres(3))
print(multiplo_tres2(8))
print(multiplo_tres3(27))
imprime_borda()

##################################################################################

#Faça uma função que retorne True se o número informado como argumento for múltiplo de 5.

def multiplo_cinco(numero: int) -> bool:    #Tradicional
    if numero % 5 == 0:
        return True
    else:
        return False

def multiplo_cinco2(numero: int) -> bool:   #ternario
    return True if numero % 5 == 0 else False

multiplo_cinco3 = lambda numero : True if numero % 5 == 0 else False

imprime_borda()
print("Exercicio 7")
print(multiplo_cinco(125))
print(multiplo_cinco2(30))
print(multiplo_cinco3(41))

##################################################################################
imprime_borda()

#Faça uma função que retorne a soma dos número informado como argumento.

def retorna_soma(num1: int, num2: int) -> int:  #tradicional
    return num1 + num2

retorna_soma3 = lambda num1, num2 : num1 + num2

#Faça uma função que retorne a diferença dos número informado como argumento.

def retorna_subtracao(num1: int, num2: int) -> int:     #tradicional
    return num1 - num2

retorna_subtracao3 = lambda num1, num2 : num1 - num2

def produto(num1: int, num2: int) -> int:   #tradicional
    return num1 * num2

produto2 = lambda num1, num2 : num1 * num2

def produtoA(*numeros: tuple) -> int:
    resultado = 1
    for i in numeros:
        resultado *= i
    
    return resultado

produtoB = lambda *numeros : produtoA(numeros)



print("Exercicios de 8 a 10")

A = int(input("Digite um valor: "))
B = int(input("Digite o segundo valor: "))

imprime_borda()
print("Exercicio 8")
print(retorna_soma(A, B))
print(retorna_soma3(A, B))

imprime_borda()
print("Exercicio 9")
print(retorna_subtracao(A, B))
print(retorna_subtracao3(A, B))

imprime_borda()
print("Exercicio 10")
print(produto(A, B))
print(produto2(A, B))

imprime_borda()
print("Exercicio 10 - variacao")
print(produtoA(A, B))
print(produtoB(A, B))
