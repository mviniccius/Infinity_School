#importando
from calcula import Calculadora

#fazendo o menu para utilizar a calculadora
#utilizando estrutura de repeticao para fazer o menu:

while True:
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("4 - Subtrair")
    print("5 - Sair do programa")
    menu = int(input("Digite a opcao desejada: "))
#entrada dos valores
#criando a calculadora
    calculadora = Calculadora(num1, num2)
    num1 = int(input("Digite o primeiro valor"))
    num2 = int(input("Digite o segundo valor"))

    if menu == 5:
        #chamar funcao para sair
        break    
    elif menu == 1:
    #chamar funcao
        print(calculadora.soma_numeros())    

    elif menu == 2:
        print(calculadora.multiplica_numeros())
            
    elif menu == 3:
        print(calculadora.divide_numeros())
    
    elif menu == 4:
        print(calculadora.subtrai_numeros())
    else:
        print("Opcao invalida")
    
