from abc import ABC, abstractmethod
# Herança Simples - Vou utilizar o exemplo do arquivo system.escola.py

# Vou usar aqui também o exemplo de Polimofismo, Classes Abstratas e Heranças Multiplas

# Classe Abstrata
class Pessoa(ABC):

    # Super classe ou classe mãe

    def __init__(self, nome=None, data=None, cpf=None, rg=None):
        self.nome = nome
        self.data_nascimento = data
        self.cpf = cpf
        self.rg = rg
        print("Construtor")

    def imprimir_nome(self):
        return self.nome

    @abstractmethod     #Método da classe abstrata porq não herdar da classe ABC 
    def trabalhar(self):
        pass

# Classes concreta
class Administrador(Pessoa):                           # Aqui, o método trabalhar() na classe Administrador retorna a string "Analisando… ", 
    def trabalhar(self):                         # que é diferente do método trabalhar() na superclasse Pessoa.
        nome_classe = self.__class__.__name__    # Indicando o Polimofismo
        return "Analisando... "

# Classes concreta   
class Professor(Pessoa):
    # Subclasse ou classe filho

    def __init__(self, nome):
        super().__init__(nome)
        self.disciplinas = []


    def trabalhar(self):
        nome_classe = self.__class__.__name__
        return "Ensinando... "

# Classes concreta
class Aluno():
   # Subclasse ou classe filho

    def __init__(self, nome):
        super().__init__(nome)
        self.matricula = None
        self.notas = []


    def estudar(self):
        return "Estudando... "

