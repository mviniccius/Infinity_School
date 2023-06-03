'''
leia um numero
imprima esse numero de 1 até o mesmo e o inverso.
ex: 5 => 12345
'''

num = int(input("Digite um valor inteiro para imprimir o intervalo entre 1 e o numero digitado: "))
numero = " "
numero_inverso = " "
for i in range(0, num):
    numero = numero + str(i+1)
    
print(numero)
i = num
while i > 0:
    numero_inverso = numero_inverso + str(i)
    i -= 1
print(numero_inverso)