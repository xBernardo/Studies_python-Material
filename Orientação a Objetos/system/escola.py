
# Name Mangling _Classe__atributo

class Quadrado:
    

    def __init__(self, lado):
        self.__lado = lado
        self.__area = lado * lado
    

    def retornaArea(self):
        print(self.__area)


quadrado = Quadrado(6)
quadrado.retornaArea()
quadrado.area = 7   # Atributo dinânimico que não foi acessado no atributo privado
quadrado.retornaArea()
print(quadrado.__dict__)
quadrado._Quadrado__area = 13 # Acessando o valor de area no name mangling
quadrado.retornaArea()