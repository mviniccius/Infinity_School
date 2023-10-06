from crud import CRUD


registro = CRUD('db.db', 'admin', 'admin')

menu = True
while menu:
    
    print("1 - Cadastrar")
    print("2 - Imprimir lista")
    print("3 - Atualizar cadastro - TOTAL")
    print("4 - Deletar por ID")
    print("0 - Sair", end="\n\n")
    
    controle = input("Escolha a opcao desejada!\n")

    if controle == '1':
        print("Entrou na opcao de cadstro\n")
        nome = input("Digite o nome:\n")
        idade = input("Digite a idade:\n")
        registro.criar(nome, idade)
        print()

    elif controle == '2':
        print("Imprimir lista completa:\n")
        lista = registro.ler_tudo()
        print(lista)
        print()

    elif controle == '3':
        print("Entrou")
    
    elif controle == '4':
        print("Entrou")
        print()
    elif controle == '0':
        menu = False
    
    else:
        print("Opcao invalida")
    
print("Obrigado por utilizar o sistema")