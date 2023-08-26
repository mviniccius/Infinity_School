class Calculadora:
    def __init__(self, num1:int, num2:int) -> None:
        self.num1 = num1
        self.num2 = num2
        pass
    
    
    def soma_numeros(self) -> int:
        return self.num1 + self.num2
    
    def subtrai_numeros(self) -> int:
        return self.num2 - self.num1
    
    def multiplica_numeros(self) -> int:
        return self.num1 * self.num2
    
    def divide_numeros(self) -> int:
        return self.num1 / self.num2

if __name__ == 'name':
    nova_calculadora = Calculadora()
    print(nova_calculadora.soma_numeros(1,2))