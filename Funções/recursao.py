
# Resolver um fatorial de uma função

"""
def reduzir_num(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzir_num(10)
"""

"""
1 - checa se o numero não é igual a 0
2- Se ele não for igual a 0 nós vai reduzir em 1 unidade

5 (N - 1)
  4 (5 - 1)
    3 (4 - 1)
      2 (3 - 1)
        1 (2 - 1)
          0 (1 - 1)

"""

"""
def reduzir_num(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        #remover uma unidade desse número -1 
        reduzir_num(numeroInt - 1)


reduzir_num(8)
"""

# Fatorial sem recursão

def fatorialS(numero):
    fatorial = 1 
    if numero == 0: # Critério de parada
        return 1
    else:
        # Parametro da chamada recursiva
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial


print(fatorialS(5))


# Fatorial recursivo

def fatorialR(numero):
    if numero == 0: # Critério de parada
        return 1 
    else:
        # Parametro da chamada recursiva
        return numero * fatorialR(numero - 1) 


print(fatorialR(3))

"""
5! = 5*4!
   = 5*4*3!
   = 5*4*3*2!
   = 5*4*3*2*1!

4! = 4*3!
   = 4*3*2!
   = 4*3*2*1!

3! = 3*2*1!
   = 3*2!

2! = 2*1
   = 2*1!
...

"""