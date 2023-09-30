import sqlite3 as sql

class CRUD:
    def __init__(self, nome_banco_dados: str, user_banco_dados: str, pass_bando_dados: str) -> None:
        self.banco_dados = nome_banco_dados
        self.usuario     = user_banco_dados
        self.senha       = pass_bando_dados
        self.conexao     = None
        self.cursor      = None    
    
    def __logar(self) -> bool:
        credenciais = ('admin', 'admin')
        
        return True if self.usuario == credenciais[0] and self.senha == credenciais[1] else False
    
    def __conectar(self) -> bool:
        if self.__logar() == True:
            self.conexao = sql.connect(self.banco_dados)
            self.cursor = self.conexao.cursor() 
        return True
            
    def __desconectar(self) -> bool:
        self.conexao.close()
        return True
    
    def criar(self, nome :str, idade: int) -> None:
        if self.__conectar() == True:            
            self.cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", (nome, idade))
            self.conexao.commit()
            self.__desconectar()
            
    
    def ler_id(self, id: str) -> tuple: #Metodo para ler um registro da tabela
        if self.__conectar() == True:
            consulta = self.cursor.execute("SELECT nome, idade FROM pessoas WHERE id ?", (id,)).fetchall()
            self.__desconectar()
            return consulta
    
    def ler_tudo(self) -> list: #Metodo para ler todos os registros da tabela
        if self.__conectar() == True:
            dados = self.cursor.execute("SELECT * FROM pessoas").fetchall()
            self.__desconectar
            return dados
    
    def atualizar(self, nome: str, idade: str, id: str) -> None:
        if self.__conectar() == True:
            self.cursor.execute("UPDATE pessoas SET nome = ?, idade = ?, id = ?", (nome, idade, id))
            self.conexao.commit()
            self.__desconectar()
            
    def apagar(self, id: str) -> tuple:
        backup = self.ler_id(id)
        self.cursor.execute("DELETE FROM pessoas WHERE id = ?", (id,))
        self.conexao.commit()
        self.__desconectar()
        
        return backup