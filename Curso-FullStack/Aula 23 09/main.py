from pacote.cadastro import Cadastro as Cad
import sqlite3 as sql

controle = True #controle para saida do while

#variavel de conexao
conexao = sql.connect("bancodedados.db")

#Variavel cursor
cursor = conexao.cursor()

while controle:
    print("1 - Cadastrar")
    print("2 - Consultar por ID")
    print("3 - Listar cadastro")
    print("0 - Sair", end='\n\n')

    opcao = input("Informe uma opção: ")

    if opcao == '1':
        nome = input("Informe o nome: ")
        idade = input("Informe a idade: ")
        
        #Adicionando informacoes no BD
        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES(?, ?)", (nome, idade))
                
        #comitar as informacoes no banco, salvar
        conexao.commit()
        usuario_cadastrado = cursor.execute("SELECT * FROM pessoas").fetchall()
        print(f"Usuario ID {usuario_cadastrado[-1][0]} cadastrado com sucesso!")
    elif opcao == '2':
        dado = cursor.execute("SELECT nome, idade FROM pessoas WHERE id = ?", (3,)).fetchall()
       
        cadastro = Cad(dado[0][0], dado[0][1])
       
        print(dados)
        
    elif opcao == '3':
        #consulta ao banco de dados
        dados = cursor.execute("SELECT * FROM pessoas").fetchall() # funcao para pegar conteudo do endereco de memoria
             
        for dado in dados:
            cadastro = Cad(dado[1], dado[2])
            cadastro.mostrar_cadastro()
    
    elif opcao == '0': #condicao de saida
        controle = False
    else:
        print("Opção inválida, tente de novo...")

#fechar conexao
conexao.close()