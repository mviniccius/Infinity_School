menu = True

while menu:
    print("1 - Cadastrar cliente")
    print("2 - Listar clientes")
    print("3 - Adicionar produto")
    
    print("0 - Sair")

    menu1 = input("Digite a opcao desejada: \n")
    match menu1:
        case '1':
            print("entrou")
        case '2':
            print("entrou")
        case '3':
            pass
        case '0':
            menu = False
        case _:
            print("\nOpcao invalida\n\n")