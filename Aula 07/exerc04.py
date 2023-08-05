def verifica_senha(password):
    conta_caracter = len(password)
    count_num = 0
    count_caracter = 0
    count_pontuacoes = 0
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    pontuacoes = [',', '.', '!', '?', ';', ':']
    for caract in password:
        if caract in numbers:
            count_num +=1
        if caract.isalpha():
            count_caracter += 1
        if caract in pontuacoes:
            count_pontuacoes += 1
            
            
   # return conta_caracter, count_num, count_caracter, count_pontuacoes
    if count_caracter <= 5:
        return "Senha fraca"
    elif count_caracter > 0 and count_num > 0 and count_pontuacoes == 0:
        return "Senha forte"
    elif count_caracter > 0 and count_num > 0 and count_pontuacoes > 0:
        return "Senha muito forte"
resultado = verifica_senha("123456789")
print(resultado)