from bibliotecas.pessoa import Pessoa
from bibliotecas.funcionario import Funcionario

pessoa1 = Pessoa(
    nome = "marcao",
    sobrenome = "Viniccius", 
    idade = 30, 
    naturalidade = "BH",
    nacionalidade ="BR", 
    data_nascimento = "06/07/1993", 
    numero_id = "123456", 
    filiacao=("Bento", "Monica")
    )

pessoa1.certidao_nascimento()
print()
novo_funcionario = Funcionario(
    nome = "marcao",
    sobrenome = "Viniccius", 
    idade = 30, 
    naturalidade = "BH",
    nacionalidade ="BR", 
    data_nascimento = "06/07/1993", 
    numero_id = "123456", 
    filiacao=("Bento", "Monica"),
    cargo = "Estagiario",
    setor="RH",
    data_contratacao="10/10/2022",
    salario= 1300.00
)

novo_funcionario.cracha_funcionario()