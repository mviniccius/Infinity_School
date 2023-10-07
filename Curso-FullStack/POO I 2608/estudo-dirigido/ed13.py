""" PROGRAMAÇÃO ORIENTADA A OBJETOS (POO) - MÉTODO CONSTRUTOR """

# Se você chegou até aqui, imagino que tenha conhecido o Igor! Pois é,
# ele é muito importante na classe, pois fará a CONSTRUÇÃO do nosso objeto.
# Ou seja, ele monta tudo e deixa certinho para funcionar. Por isso que, ao
# informamos ATRIBUTOS à classe, ou características ao Cachorro, você tem que
# informar esses valores à classe. Só assim é possível construí-la.
#
# Veja o exemplo abaixo:



class Celular:
    def __init__(self, marca: str, modelo: str, valor: str) -> None:
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
    
    def mostrar_especificacoes(self):
        print(f"\nMarca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Valor: R$ {self.valor}\n")



novo_celular1 = Celular('Xiaomi', 'Readmi Note 54', 4000.0)

novo_celular1.mostrar_especificacoes()

# Com o 'novo_celular1' devidamente criado, tente utilizar a função
# mostrar_especificacoes(). O que aconteceu?
#
# Resposta:
