#Escreva um programa que leia um número inteiro positivo do usuário e imprima todos os números pares entre 0 e o número digitado.

num = int(input('digite um numero'))
for i in range(1, num):
    if (i % 2 == 0):
        print(i)
