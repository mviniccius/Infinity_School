from pacote.cadastro import Cadastro as Cad
import sqlite3 as sql

controle = True

# Variável de conexão
conexao = sql.connect("bancodedados.db")

# Variável cursor
cursor = conexao.cursor()

while controle:
    print("1 - Cadastrar pessoa")
    print("2 - Consultar por ID")
    print("3 - Listar cadastros")
    print("4 - Atualizar cadastro") # Adicionar funcionalidade
    print("5 - Deletar cadastro") # Adicionar funcionalidade
    print("0 - Sair", end='\n\n')

    opcao = input("Informe uma opção: ")

    if opcao == '1':
        nome = input("Informe o nome: ")
        idade = input("Informe a idade: ")

        # Adicionando cadastros no banco de dados
        cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))

        # Comitar as informações no banco
        conexao.commit()
        usuario_cadastrado = cursor.execute("SELECT * FROM pessoas").fetchall()
        print(f"Usuário ID {usuario_cadastrado[-1][0]} cadastrado com sucesso!")
        
    elif opcao == '2': #Inserir ID
        id = input("Digite o ID que voce deseja ")
        
        dado = cursor.execute("SELECT nome, idade FROM pessoas WHERE id = ?", (id,)).fetchall()
        cadastro = Cad(dado[0][0], dado[0][1])
        cadastro.mostrar_cadastro()
        
    elif opcao == '3':
        # Consulta ao banco de dados
        dados = cursor.execute("SELECT * FROM pessoas").fetchall()

        for dado in dados:
            cadastro = Cad(dado[1], dado[2])
            cadastro.mostrar_cadastro()
            
    elif opcao == '4':
        nome = input("Informe o nome: ")        
        idade = input("Informe idade: ")        
        id = input("Informe o ID")
        
        #Executar a atualizacao de dados
        cursor.execute("UPDATE pessoas SET nome = ?, idade = ? WHERE id = ?", (nome, idade, id))   
        #Salvar comando SQL
        conexao.commit()
             
    elif opcao == '5':
        id = int(input("Digite o ID que deseja excluir: "))
        #Executar o delete passando como parametro o ID ppara exclusao
        cursor.execute("DELETE FROM pessoas WHERE id = ?", (id,))
        #Salvar comando SQL
        conexao.commit()
    
    
    elif opcao == '0':
        controle = False
    else:
        print("Opção inválida, tente de novo...")


# Encerrando a conexão com o banco de dados
conexao.close()