#verificar se o numero eh par sem converveter para INT
par = lambda string : True if string[-1] in '02468' else False
#verifica se o numero eh negativo
negativo = lambda string: True if string[0] == '0' else False
#primeiro exemplo
print(par("15"))

numero = input("Digite um numero")
#exemplo de ternario no print
print(f"o numero {numero} eh par" if par(numero)else f"O numero {numero} eh impar")
