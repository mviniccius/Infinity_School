from crud import CRUD

registro = CRUD('db.db', 'admin', 'admin')

menu = True
while menu:
    
    print("0 - Sair")
    print("1 - Cadastrar")
    print("2 - Imprimir lista")
    print("3 - Atualizar cadastro - TOTAL")
    print("4 - Deletar por ID", end="\n\n")
    controle = input("Escolha a opcao desejada!\n")

    if controle == '1':
        print("Entrou")

    elif controle == '2':
        print("Entrou")

    elif controle == '3':
        print("Entrou")
    
    elif controle == '4':
        print("Entrou")
        
    elif controle == '0':
        menu = False
    
    else:
        print("Opcao invalida")
    
print("Obrigado por utilizar o sistema")