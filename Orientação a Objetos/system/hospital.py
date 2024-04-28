from datetime import date

class Paciente:

    def __init__(self, nome, idade, cpf, email): # Objeto que se refere a si mesmo
        print("Acessando o costrutor")
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf 
        self.email = email


    @classmethod
    def idadeAnoNascimento(cls, nome, anoNascimento, cpf, email):
        idade = date.today().year - anoNascimento
        return cls(nome, idade, cpf, email)


class Medico:
    pass


# paciente = Paciente("Cecilia Oliveira", 20, "000.000.000-00", "cecilialinda@gmail.com")
# print(paciente.__dict__)
# print(Paciente.idadeAnoNascimento(2003))

paciente = Paciente.idadeAnoNascimento("Cecilia Oliveira", 2003, "000.000.000-00", "cecilialinda@gmail.com")
print(paciente.__dict__)
print(paciente.idade)