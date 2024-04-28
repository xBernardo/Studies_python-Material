lista = ["Lancer", "Golzin", "Celta", "Alfa Romeo"]
print(lista)

numero = lista
print(numero)

"""lista = lista + numero
print(lista)"""
 
"""lista.extend(numero) #Concatenar uma lista na outra
print(lista)"""

"""for x in numero:
    lista.append(x) #concaternar umsa lista na outra da mesma lista
 
print(lista)"""

numero = lista.copy()
print(numero)