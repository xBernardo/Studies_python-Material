#import random -              1 forma de importação

# from random import choice - 2 forma de importação

"""from random import (  #-   3 forma de importação
    random,
    choice,
    uniform
)"""


from random import (     #    4 forma de importação
    random as rd
)

print(rd())

"""lista = ["pedra", "papel", "tesoura"]
print(choice(lista))

for x in range(1, 9):
    print(x)"""