#Crie um programa que leia dois valores e mostre um menu para calcular.

while True:
    print("1 - Somar")
    print("2 - Multiplicar")
    print("3 - Dividir")
    print("4 - Subtrair")
    print("5 - Sair do programa")
    menu = int(input("Digite a opcao desejada: "))    
    
    if menu < 1 or menu > 5:
        print("Opcao invalida!")
    else:
        if menu == 5:
            break
        else:
            num1 = int(input("Digite o primeiro valor: "))
            num2 = int(input("Digite o degundo valor: "))        

            if menu == 1:
                soma = num1 + num2
                print("O resultado da soma = ", soma)
            if menu == 2:
                multiplicar = num1 * num2
                print("O resultado da soma = ", multiplicar)
            if menu == 3:
                dividir = num1 / num2 
                print("O resultado da divisao = ", dividir)
            if menu == 4:
                subtrair = num1 - num2
                print("O resultado da subtracao = ", subtrair)

print("Obrigado por utilizar!")