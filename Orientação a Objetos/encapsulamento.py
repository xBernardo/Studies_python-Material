
# Nesse exemplo de encapsulamento, estou usando o script do arquivo banco.py,
# para utilizar como exemplo.

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
        self.__historico = [saldo]


    def saldo(self):
        print(f"Saldo : R${self.__saldo}")

    
    def transacao(self, saldo):
        self.__historico.append(saldo)

    
    def extrato(self):
        print("----Extrato----")
        print("Conta: ", self.titular)
        for saldo in self.__historico:
            print(f"Saldo : R${self.saldo}")


    def depositar(self, valor):
        self.__saldo += valor
        self.transacao(self.__saldo)


    def sacar(self, valor):
        self.__saldo -= valor
        self.transacao(self.__saldo)

    
    def transferir(self, valor, destino):  #Encapsulamento reduzindo a forma de processo
        self.sacar(valor)
        destino.depositar(valor)


conta1 = Conta(234, "Rodrigo", 5200)
conta2 = Conta(567, "Bernardo", 3100)

conta1.transferir(300, conta2)
conta1.saldo()
conta2.saldo()
conta1.extrato()