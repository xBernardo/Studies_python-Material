"""
Numéros Primos
"""

def primo(numero):
    if numero > 1:
        for x in range (2, numero):
            if(numero % x) == 0:
                return"Esse não é primo mano!"
        else:
            return "Ele é primo mano!"
    else:
        return"Esse número não é primo: Número menor ou igual a 1"