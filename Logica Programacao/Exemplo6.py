#Escreva um programa que leia uma lista de números inteiros do usuário e encontre o maior número da lista usando uma estrutura for.
maior_numero = 0
for i in range(0, 5):
    num = int(input('digite um numero '))
    if (num > maior_numero):
        maior_numero = num
print(maior_numero)
