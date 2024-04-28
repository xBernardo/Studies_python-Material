#                                Paradgma Orientado a Objetos 

# Classe - Um conjuno de objetos com a mesma caracteristicas
# Objeto- Representação do mundo real como um tipo de dado de uma classe
# Construtor - É uam função criada implicitamente com mesmo nome da classe
# Atributos - São as váriaveis de uma classe


def Registro(nome, idade, cpf, email):
    paciente = {"Nome": nome, "Idade": idade, "CPF": cpf, "Email": email}
    return paciente
# Reuso e Coesão


#                                      Classes e Objetos

class Paciente:
    
    def __init__(self, nome, idade, cpf, email): # Objeto que se refere a si mesmo
        print("Acessando o costrutor")
        self.nome = nome 
        self.idade = idade
        self.cpf = cpf 
        self.email = email


"""
#                                                     (arquivo.py)         (Classe)                                              
Todos os comando são feitos no terminal usando o from classe_objeto import Paciente
"""

"""
                                   + Sobre Classes

Simulaççao de Eventos Discretos
Relação -> Destacando dunções e varieaveis

--------------------------

Conceitos Estruturais

- Classe

Classe é uma estrutura que abstreai um conjunto de objetos com caracateristicas
similares. Definindo o comportamaneto dos seus objetos através ds estruturas:

1 - Atributos
2 - Métodos

A classse define um tipo de dados abstrato

---------------------------

Conceitos Fundamentais

- Abstração

Processo pelo qual se isolam atributos de um objeto.
consederando os que certos grupos de objetos tenham em comum

- Reúso

Não existe prática em programação do que repetir códigos

"""