#importando objeto
from pacote.jogador import Jogadores

controle = True

lista_de_jogadores = []

while(controle):
    
    print("\n\nSistema FIFA")
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("0 - SAIR")

    menu = input("Escolha a opcao desejada\n")

    if menu == '1':
        print("Cadastro Jogador")
        nome = input("Digite o nome:\n")
        nome_do_time = input("Digite o time:\n")
        numero_camisa = input("Digite o numero da camisa\n")

        jogador = Jogadores(nome, nome_do_time,numero_camisa)

        lista_de_jogadores.append(jogador) #Adicionando jogador a uma lista

    elif menu == '2':
        print("\nDados dos jogadores")
        
        for jogador in lista_de_jogadores:
            print(f"Nome:{jogador.nome}\nTime: {jogador.nome_do_time}\nNumero da camisa: {jogador.numero_camisa}")
    
    elif menu == '0':
        controle = False

    else:
        print("Opcao invalida")
        

print("saiu!")