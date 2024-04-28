
# Parametros Padrão - define argumentos não obrigatórios

"""def imprimir(nome=None, sobrenome=None, idade=None):
    if nome != None:
        print("nome: ", nome)
        print("sobrenome: ", sobrenome)
        print("idade: ", idade)
        print("-----------------")
    else:
        print("Insira seus dados")
        print("-----------------")

imprimir()
imprimir("Bernardo", "Silva", 26)
"""

def imprimir_carro(marca, chassi, placa=None):
    print("----------------")
    print("Marca: ", marca)
    print("Chassi:", chassi)
    if placa != None:
        print("Placa do carro é: ", placa)


print()
#  Exemplos de nº de argumentos <= nº dps parametros
imprimir_carro("Conssecionária - PE", 3)
imprimir_carro("Loja - SP", 2, 1)


