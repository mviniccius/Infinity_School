#importando objeto
from pacote.jogador import Jogadores

controle = True

lista_de_jogadores = []
lista_de_times = []

while(controle):
    
    print("\n\nSistema FIFA")
    print("1 - Cadastrar jogador")
    print("2 - Listar jogadores")
    print("3 - Listar times")
    print("4 - Jogadores do time")
    print("0 - SAIR")

    menu = input("Escolha a opcao desejada\n")

    if menu == '1':
        print("Cadastro Jogador")
        nome = input("Digite o nome:\n")
        nome_do_time = input("Digite o time:\n")
        
        numero_camisa = input("Digite o numero da camisa\n")
        # if nome do time senao cadastrar dentro do while
        jogador = Jogadores(nome, nome_do_time,numero_camisa)
        # Adicionar novo Time se nao existir
        
        if nome_do_time not in lista_de_times:
            lista_de_times.append(nome_do_time)
        lista_de_jogadores.append(jogador) #Adicionando jogador a uma lista

    elif menu == '2':
        print("\nDados dos jogadores")
        
        for jogador in lista_de_jogadores:
            print(f"Nome:{jogador.nome}\nTime: {jogador.nome_do_time}\nNumero da camisa: {jogador.numero_camisa}")
    
    elif menu == '3':
            for time in lista_de_times:
                 print(time)

    elif menu == '4':
            time = input("Digite o nome do time para imprimir os jogadores")
            
            if time not in lista_de_times:
                 print("Nao existe o time informado")
            else:
                 if jogador.jogador_no_time in lista_de_times:
                      print(jogador.jogador_no_time)
                
    elif menu == '0':
        controle = False

    else:
        print("Opcao invalida")
        

print("saiu!")