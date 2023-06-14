# Desafio: Crie um algoritmo que recebe dois valores númericos e qual operação o usuário deseja realizar e realize essa operação. 
# Por exemplo: O usuário forneceu as seguintes entradas: 4, 5, multiplicação. Ele deseja multiplicar 4 e 5 e ser informado do resultado. 
# Mas numa próxima execução do programa talvez ele queira utilizar outros valores ou fazer outra operação... e aí, como fazer?

menu = -1
while menu != 5:
    print("Mini calculadora!")
    print("[ 1 ] - Soma")
    print("[ 2 ] - Subtracao")
    print("[ 3 ] - Multiplicar")
    print("[ 4 ] - Dividir")
    print("[ 5 ] - Sair")
    menu = input("Escolha a opcao desejada ou 5 para sair: \n")  
    while menu.isnumeric() != True:
        print("Voce nao digitou um numero, digite novamente!\n")
        print("Mini calculadora!")
        print("[ 1 ] - Soma")
        print("[ 2 ] - Subtracao")
        print("[ 3 ] - Multiplicar")
        print("[ 4 ] - Dividir")
        print("[ 5 ] - Sair")  
        menu = input("Escolha a opcao desejada ou 5 para sair: \n")  
    if(int(menu) < 0 or int(menu) > 5):
        print("Opcao invalida\n\n")       
        continue
    else:
        if(menu == 5):
            break
        else:
            num1s = input("Digite um valor: ")
            while num1s.isnumeric() != True:
                print("Voce nao digitou um numero\n")
                num1s = input("Digite um valor: ")
            num2s = input("Digite outro valor: ")
            while num2s.isnumeric() != True:
                print("Voce nao digitou um numero\n")
                num2s = input("Digite um valor: ")
            num1 = int(num1s)
            num2 = int(num2s)
            if(menu == '1'):
                print("\nA soma do", num1, "+", num2,"=", num1 + num2)
            elif(menu == '2'):
                print("\nA subtracao do", num1, "-", num2,"=", num1 - num2)
            elif(menu == '3'):
                print("A multiplicacao do", num1, "X", num2,"=", num1 * num2)
            elif(menu == '4'):
                print("\nA divisao do", num1, "/", num2,"=", num1 / num2)     
print("Obrigado por utilizar!")