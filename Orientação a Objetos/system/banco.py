"""
Visibilidade - Modificador de Acesso
 
privada (private) - restritiva -> Define que os atributos e metódos só podem ser
manipulados dentro da classe.

protegida (protected) - intermediária -> Define que os atributos e métodos só podem ser 
manipulados dentro da classe e nas classes que herdam da calsse onde foram definidas .

pública (public) - menos restritiva -> Define que os atributos e métodos são acessiveis
em qualquer lugar.
"""

class Conta:

    #Atributos de Classe 
    taxa = 0.50
 
    @classmethod            # Recebe parametros de referencia da classe
    def retornarCodigo(cls):
        print("Codigo: 555")

    
    @staticmethod           # Parametros que ele pode receber e não consegue acessar os mtd da classe
    def retornarCodigoBanco():
        return "999"

    # Atributos de Instâncias
    def __init__(self, numero, titular, saldo):
        self._numero = numero  # Visibilidade protegida (protected)
        self.titular = titular # Visibilidade pública (public)
        self.__saldo = saldo   # Visibilidade privada (private)


    def extrato(self):
        
        #self.saldo -= Conta.taxa -> Referência a classe e não a instância
        print(f"Saldo : R${self.__saldo}")


    def depositar(self, valor):
        self.__saldo += valor


    def sacar(self):
        self.__saldo -= valor 


# Instâncias da Classe Conta
conta1 = Conta(123, "Rodrigo Bernardo", 5500)
conta2 = Conta(456, "Bernardo Silva", 7200)

#print(f"Titular : {conta1.titular} - Saldo: R${conta1.saldo}")
#print(f"Titular : {conta2.titular} - Saldo: R${conta2.saldo}")

print(conta1.__dict__)
print(conta2.__dict__)

conta2.extrato()

# Atributo Dinâmico -> Criado em tempo de execusão
conta2.apelido = "Dom"

print(conta1.__dict__)
print(conta2.__dict__)

del conta2.apelido

print(conta2.__dict__)

# Método da classe
Conta.retornarCodigo() # Convenção da nossa classe
conta1.retornarCodigo() # Acessando o método da classe

# Método Estático 
print(Conta. retornarCodigoBanco()) # Convenção do método estático 
print(conta2.retornarCodigoBanco())

