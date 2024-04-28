
"""
Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas
chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global
deve ser impresso o resultado retornado por estas funções.
    a) Uma função que receba X e Y como entrada e retorne o maior deles;
    b) Uma função que receba X e Y como entrada e retorne a média aritmética deles;
"""

def numero_maior(x, y):
    return max(x, y)

def media_numero(x, y):
    return (x + y) / 2

x = float(input("Qual o número do x: "))
y = float(input("Qual o número do y: "))

print(f"O maior número entre {x} e {y} é: {numero_maior(x, y)}")
print(f"A média aritmética entre {x} e {y} é: {media_numero(x, y)}")