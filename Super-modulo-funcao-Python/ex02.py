def fatorial(n: int):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i += 1
        
    print("O valor de %d! eh =" %n, fat)

n = int(input("Digite o valor de n: "))
fatorial(n)