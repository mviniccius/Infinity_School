from random import randint 

num_aleatorio = randint(0, 100)
print(num_aleatorio)


print("_____________________________________________________________________________")
print("                                     BEM VINDO                               ")
print("_____________________________________________________________________________")
menu = int(input("Digite 1 para joga ou 0 para sair! "))
while menu != 0:
    tentativa = 1

    palpite = input("Digite um valor entre 0 e 100: ")
    #primeira conferencia se foi digitado numero
    while palpite.isnumeric() != True:
        palpite = input("Opcao invalida voce digitou um texto! Digite novamente: ")
    while int(palpite) != num_aleatorio:
        #conferir input
        if palpite.isnumeric() == True:
        #conferir se está dentro do range de 0 a 100
            if int(palpite) >= 0 and int(palpite) <= 100:
                if int(palpite) < num_aleatorio:
                    print("O numero digitado é menor que o numero secreto!")
                    tentativa += 1
                else:
                    print("O numero digitado é maior que o numero secreto!")  
                    tentativa += 1  
        else:
            print("Opcao invalida!")        
        palpite = input("Digite um valor entre 0 e 100: ")
        #conferir se valor eh verdadeiro antes de voltar no loop
        while palpite.isnumeric() != True:
            palpite = input("Opcao invalida voce digitou um texto! Digite novamente: ")
    print("Foram", tentativa,"tentativas!")
    print("[ 1 ] - sim")
    print("[ 2 ] - nao")
    menu = int(input("Deseja jogar novamente?"))    
