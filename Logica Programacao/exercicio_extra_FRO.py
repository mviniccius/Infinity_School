salario_mais_tres_filhos = 0
quantidade_cidadao_salario_ate_1500 = 0

for i in range(0, 5):
    salary = float(input("Digite o valor do salario: "))
    if salary <= 1500:
        quantidade_cidadao_salario_ate_1500 += 1
    children = int(input("Digite a quantidade de filhos: "))
    if children > 3:
        salario_mais_tres_filhos += salary

print(f"Existem {quantidade_cidadao_salario_ate_1500} que recebem salario de ate R$1500.00")
print(f"A soma dos salarios das pessoas que tem mais de tres filhos: {salario_mais_tres_filhos}")