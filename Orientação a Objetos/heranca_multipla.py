
# Herança Mútiplas

class Funcionario:

    def trabalhar(self):
        print("Trabalhando...")

    
class FrontEnd(Funcionario):

    def front_end(self):
        super().trabalhar()


class BackEnd(Funcionario):

    def back_end(self):
        super().trabalhar()


class FullStack(BackEnd, FrontEnd): # Exemplo de Herança Multipla, herdando da classe Frontend e Backend
    
    def trabalhar(self):
        print("Full Stack")


bernardo = FrontEnd()
cayton = BackEnd()

bernardo.trabalhar()
cayton.trabalhar()

rodrigo = FullStack()
rodrigo.trabalhar()