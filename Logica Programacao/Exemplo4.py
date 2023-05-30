#Escreva um programa que leia um número inteiro positivo do usuário e imprima a soma de todos os números ímpares entre 1 e o número digitado.
impar = 0
num = int(input('digite um numero'))
for i in range(0, num):
    if (i % 2 != 0):
        impar = i + impar
print(impar)
