
#        COLEÇÃO ORDENNADA, MUTÁVEL E QUE PERMITE VALORES DUPLICADOS

"""lista = []
print(lista)
print (len(lista))
print (type(lista))

print("-"*50)

tupla = ("item1", "item2", "item3", "item1", "item1")
print(tupla)
print (len(tupla))
print (type(tupla)) 

print(tupla.count("item1")) #Usado para contar quantas vezes existe o mesmo elemento no index
"""

"""uf = ("PE", "AL", "PB", "CE") #Usa-se tupla para que valores não sejam mudados no final
print(type(uf))

lista = list(tupla)
print(tupla)
print(lista)

lista.pop() #editando minha lista
print(lista)



tupla = tuple(lista) #Transformando minha tupla em lista para ser editada
#del tupla            # Deletando a tupla
print(tupla)"""


                                    # LOOPS! tupla


tupla = ("Sport", "Santos", "Man United", "Nautico", "Santa Cruz")
print(tupla)

"""(x, y, z) = tupla #empacotamento e desencopamento
print("x: ", x)
print("y: ", y)
print("z: ", z)"""


(x, *y, z) = tupla 
print("x: ", x)
print("y: ", y)
print("z: ", z)
