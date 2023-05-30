while True:
    sexo = input("Digite o sexo(M/F)")
    if sexo == 'F' or sexo == 'M':
        break
    else:
        print("Opcao invalida!")
print("O sexo digitado foi:", sexo)
