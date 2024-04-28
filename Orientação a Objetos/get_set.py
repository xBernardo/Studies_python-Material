
# Métodos Getters e Setters - Vou utilizar o exemplo do arquivo escola.py

class Aluno:

    def __init__(self, nome, idade, matricula, notas):
        self.__nome = nome
        self._idade = idade
        self.__matricula = matricula
        self.__notas = None

    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def idade(self):
        return self._idade


    @idade.setter
    def idade(self, idade):
        self._idade = idade


aluno1 = Aluno("Cayton", 19, 00000, 7)

print(aluno1.nome)
"""print(aluno1.get_idade())
print(aluno1.get_matricula())
print(aluno1.get_notas())"""
print(aluno1.nome)
aluno1.nome = "Pirraia Filho"
print(aluno1.nome)